"use client";

/**
 * NEXUS STORE - HOME PAGE
 * Features: Product Stock Display & Out-of-Stock Logic
 */

import React, { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ArrowRight, ShoppingCart, ShoppingBag, ShieldCheck, Box } from "lucide-react";
import Link from "next/link";

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

interface Product {
  id: number;
  name: string;
  description: string;
  price: string;
  stock: number; // સ્ટોક એડ કર્યો
  image?: string;
}

export default function Home() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [cartCount, setCartCount] = useState(0);
  const [toast, setToast] = useState("");

  useEffect(() => {
    const getProducts = async () => {
      try {
        const response = await fetch(`${API}/get_products/`);
        const data = await response.json();
        setProducts(data);
      } catch (error) {
        console.error("Failed to fetch products:", error);
      } finally {
        setLoading(false);
      }
    };

    const updateLocalCount = () => {
      const token = localStorage.getItem("token");
      if (!token) { setCartCount(0); return; }
      const username = localStorage.getItem("username") || "guest";
      const savedCart = JSON.parse(localStorage.getItem(`cart_${username}`) || "[]");
      const total = savedCart.reduce((s: number, p: any) => s + (p.quantity || 1), 0);
      setCartCount(total);
    };

    updateLocalCount();
    getProducts();
    window.addEventListener("cartUpdated", updateLocalCount);
    window.addEventListener("storage", updateLocalCount);
    return () => {
      window.removeEventListener("cartUpdated", updateLocalCount);
      window.removeEventListener("storage", updateLocalCount);
    };
  }, []);

  const addToCart = (product: Product) => {
    // જો સ્ટોક ૦ હોય તો એડ ના થવા દેવું
   if (product.stock !== undefined && Number(product.stock) <= 0) {
    setToast("Sorry, this item is out of stock!");
    setTimeout(() => setToast(""), 2500);
    return;
}

    const token = localStorage.getItem("token");
    if (!token) { window.location.href = "/login?next=/"; return; }

    const username = localStorage.getItem("username") || "guest";
    const cartKey = `cart_${username}`;
    const existingCart = JSON.parse(localStorage.getItem(cartKey) || "[]");
    const found = existingCart.find((p: any) => p.id === product.id);
    
    if (found) { found.quantity = (found.quantity || 1) + 1; }
    else { existingCart.push({ ...product, quantity: 1 }); }
    
    localStorage.setItem(cartKey, JSON.stringify(existingCart));
    const total = existingCart.reduce((s: number, p: any) => s + (p.quantity || 1), 0);
    setCartCount(total);
    window.dispatchEvent(new Event("cartUpdated"));
    setToast(`${product.name} added to cart!`);
    setTimeout(() => setToast(""), 2500);
  };

  return (
    <main className="min-h-screen bg-gray-50 font-sans relative">

      {/* TOAST */}
      <AnimatePresence>
        {toast && (
          <motion.div initial={{ y: 60, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={{ y: 60, opacity: 0 }}
            className="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 bg-gray-900 text-white px-6 py-3 rounded-full text-sm font-bold shadow-2xl">
            🛒 {toast}
          </motion.div>
        )}
      </AnimatePresence>

      {/* ADMIN BUTTON */}
      <div className="fixed bottom-10 left-10 z-50">
        <Link href="/admin/login">
          <motion.button
            whileHover={{ scale: 1.08, x: 4 }}
            whileTap={{ scale: 0.95 }}
            className="bg-black/80 backdrop-blur-md text-white px-5 py-3 rounded-2xl shadow-2xl flex items-center gap-3 border border-white/20"
          >
            <ShieldCheck className="w-5 h-5 text-red-500" />
            <span className="font-bold text-xs uppercase tracking-widest">Admin Portal</span>
          </motion.button>
        </Link>
      </div>

      {/* FLOATING CART BUTTON */}
      <div className="fixed top-24 right-10 z-50">
        <Link href="/cart">
          <motion.button whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }}
            className="bg-red-600 text-white p-4 rounded-2xl shadow-2xl flex items-center gap-2">
            <ShoppingBag className="w-6 h-6" />
            <span className="bg-white text-red-600 px-2 py-0.5 rounded-full text-xs font-black">{cartCount}</span>
          </motion.button>
        </Link>
      </div>

      {/* HERO SECTION WITH DRAGON IMAGE */}
      <section className="relative h-[85vh] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img src="/hero-bg.jpg" alt="Hero Background" className="w-full h-full object-cover" />
          <div className="absolute inset-0 bg-black/40" />
        </div>

        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }}
          className="text-center z-10 px-6">
          <span className="text-red-500 font-bold tracking-[0.3em] uppercase text-sm mb-4 block underline decoration-red-500 underline-offset-8">
            New Season 2026
          </span>
          <h2 className="text-6xl md:text-8xl font-black tracking-tighter text-white mb-6">
            SELECT <span className="text-red-600">PREMIUM</span>
          </h2>
          <p className="text-gray-200 max-w-lg mx-auto mb-8 font-medium">
            Curated high-end tech gear for the modern professional. Unleash the power within.
          </p>
          <Link href="/shop">
            <motion.button whileHover={{ scale: 1.05 }}
              className="bg-red-600 text-white px-10 py-4 rounded-full font-bold flex items-center mx-auto gap-2 group shadow-2xl hover:bg-red-700 transition">
              Explore Collection <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition" />
            </motion.button>
          </Link>
        </motion.div>
        
        <motion.div animate={{ rotate: 360 }} transition={{ duration: 30, repeat: Infinity, ease: "linear" }}
          className="absolute w-175 h-175 border border-dashed border-white/20 rounded-full opacity-30 pointer-events-none" />
      </section>

      {/* PRODUCT LIST */}
      <section className="max-w-7xl mx-auto py-20 px-6">
        <h3 className="text-4xl font-black text-gray-900 mb-12 tracking-tight">Our Gallery</h3>

        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
            {[1, 2, 3].map((i) => <div key={i} className="h-100 bg-gray-200 animate-pulse rounded-[40px]" />)}
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
            <AnimatePresence>
              {products.map((product, index) => (
                <motion.div key={product.id} initial={{ opacity: 0, y: 30 }} whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }} viewport={{ once: true }}
                  className="group bg-white rounded-[40px] p-8 shadow-sm border border-gray-100 hover:shadow-2xl transition-all duration-500">

                  <Link href={`/product/${product.id}`}>
                    <div className="h-60 bg-gray-50 rounded-4xl mb-8 flex items-center justify-center overflow-hidden cursor-pointer relative">
                      {product.image
                        ? <img src={product.image} alt={product.name} className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
                        : <span className="text-7xl group-hover:scale-110 transition-transform duration-500">📦</span>
                      }
                      
                      {/* OUT OF STOCK OVERLAY */}
                      {product.stock <= 0 && (
                        <div className="absolute inset-0 bg-black/60 flex items-center justify-center backdrop-blur-[2px]">
                           <span className="bg-red-600 text-white px-4 py-1 rounded-full text-xs font-black uppercase tracking-widest">Sold Out</span>
                        </div>
                      )}
                    </div>
                  </Link>

                  <div className="flex justify-between items-start mb-2">
                    <Link href={`/product/${product.id}`}>
                      <h4 className="text-2xl font-bold text-gray-900 hover:text-red-600 transition cursor-pointer">{product.name}</h4>
                    </Link>
                    {/* STOCK BADGE */}
                    <span className={`text-[10px] font-black px-2 py-1 rounded-md border ${product.stock > 5 ? 'text-green-600 border-green-200 bg-green-50' : product.stock > 0 ? 'text-orange-600 border-orange-200 bg-orange-50' : 'text-red-600 border-red-200 bg-red-50'}`}>
                        {product.stock > 0 ? `${product.stock} IN STOCK` : 'OUT OF STOCK'}
                    </span>
                  </div>

                  <p className="text-sm text-gray-400 mb-4 line-clamp-2">{product.description}</p>
                  
                  <div className="flex justify-between items-center pt-6 border-t border-gray-100">
                    <span className="text-3xl font-black text-gray-900 tracking-tighter">${product.price}</span>
                    
                    {/* ADD BUTTON WITH STOCK CHECK */}
                    <motion.button 
                      whileTap={{ scale: 0.9 }} 
                      onClick={() => addToCart(product)}
                      disabled={product.stock <= 0}
                      className={`${product.stock <= 0 ? 'bg-gray-300 cursor-not-allowed text-gray-500' : 'bg-gray-900 hover:bg-black text-white'} px-8 py-3 rounded-2xl font-bold text-sm shadow-xl flex items-center gap-2 transition`}
                    >
                      {product.stock > 0 ? <><ShoppingCart className="w-4 h-4" /> Add</> : 'Unavailable'}
                    </motion.button>
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>
          </div>
        )}
      </section>
    </main>
  );
}