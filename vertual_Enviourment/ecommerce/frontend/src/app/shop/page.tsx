"use client";

import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Search } from "lucide-react";
import Link from "next/link";

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

const CATEGORIES = [
  'All', 
  'Elite Laptops', 
  'Mechanical Keyboards', 
  'Pro Peripherals', 
  'Workstation Setup'
];

export default function ShopPage() {
  const [products, setProducts] = useState<any[]>([]);
  const [filtered, setFiltered] = useState<any[]>([]);
  const [search, setSearch] = useState("");
  const [activeCat, setActiveCat] = useState("All");

 useEffect(() => {
  // સાચો API પાથ અહીં લખો (દા.ત. /get_products/ અથવા /api/products/)
  fetch(`${API}/get_products/`) 
    .then(res => {
      if (!res.ok) throw new Error("Network response was not ok");
      return res.json();
    })
    .then(data => {
      setProducts(data);
      setFiltered(data);
    })
    .catch(err => console.error('Products fetch error:', err));
}, []);

  // સુધારેલું સર્ચ અને ફિલ્ટર લોજિક
  useEffect(() => {
    let result = [...products];

    // ૧. પહેલા કેટેગરી ફિલ્ટર કરો
    if (activeCat !== "All") {
      result = result.filter(p => p.category === activeCat);
    }

    // ૨. પછી સર્ચ કીવર્ડ ચેક કરો (નામ, કેટેગરી અથવા ડિસ્ક્રિપ્શનમાં)
    if (search.trim() !== "") {
      const query = search.toLowerCase();
      result = result.filter(p => 
        (p.name?.toLowerCase().includes(query)) ||
        (p.category?.toLowerCase().includes(query)) ||
        (p.description?.toLowerCase().includes(query))
      );
    }

    setFiltered(result);
  }, [search, activeCat, products]);

  return (
    <div className="min-h-screen bg-[#050505] text-white font-sans">
      
      {/* HERO / HEADER SECTION */}
      <header className="relative h-[50vh] flex items-end pb-16 px-10 sm:px-20 overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img 
            src="/shop-header.jpg"
            className="w-full h-full object-cover opacity-60" 
            alt="Shop Background"
          />
          <div className="absolute inset-0 bg-linear-to-t from-[#050505] via-transparent to-transparent" />
        </div>

        <div className="max-w-7xl mx-auto w-full relative z-10">
          <motion.h1 
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            className="text-6xl md:text-8xl font-black tracking-tighter mb-8 italic"
          >
            THE <span className="text-red-600">BG</span> ARCHIVE
          </motion.h1>
          
          <div className="flex flex-col md:flex-row items-center gap-6">
            {/* SEARCH BOX (સુધારેલું) */}
            <div className="relative flex-1 w-full max-w-xl flex gap-3">
              <div className="relative flex-1">
                <Search className="absolute left-5 top-1/2 -translate-y-1/2 text-gray-500 w-5 h-5" />
                <input 
                  type="text" 
                  placeholder="Search name or category..."
                  value={search}
                  className="w-full bg-white/5 backdrop-blur-md border border-white/10 p-5 pl-14 rounded-3xl outline-none focus:ring-2 focus:ring-red-600 transition-all text-lg text-white"
                  onChange={(e) => setSearch(e.target.value)}
                />
              </div>
              {/* સર્ચ બટન હવે સર્ચ ક્લીયર કરવા માટે અથવા એક્શન માટે વાપરી શકાય */}
              <button
                className="bg-red-600 hover:bg-red-700 transition px-6 rounded-3xl font-bold text-white shadow-lg shadow-red-900/40"
              >
                <Search className="w-5 h-5" />
              </button>
            </div>

            {/* CATEGORIES NAVIGATION */}
            <div className="flex items-center gap-3 overflow-x-auto pb-2 w-full md:w-auto scrollbar-hide">
              {CATEGORIES.map(cat => (
                <button 
                  key={cat} 
                  onClick={() => setActiveCat(cat)}
                  className={`px-6 py-3 rounded-2xl text-sm font-bold transition-all whitespace-nowrap border ${
                    activeCat === cat 
                      ? 'bg-red-600 border-red-600 text-white shadow-lg shadow-red-900/20' 
                      : 'bg-white/5 border-white/10 text-gray-400 hover:bg-white/10 hover:border-white/30'
                  }`}
                >
                  {cat}
                </button>
              ))}
            </div>
          </div>
        </div>
      </header>

      {/* PRODUCT GRID */}
      <main className="max-w-7xl mx-auto py-20 px-10 sm:px-20 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        <AnimatePresence mode="popLayout">
          {filtered.map((product) => (
            <motion.div 
              layout 
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.9 }}
              key={product.id}
              className="bg-white/5 border border-white/10 p-6 rounded-[40px] hover:bg-white/8 hover:border-red-600/50 transition-all duration-500 group relative"
            >
              <Link href={`/product/${product.id}`}>
                <div className="h-56 bg-[#0a0a0a] rounded-[30px] mb-6 flex items-center justify-center overflow-hidden relative shadow-inner">
                  {product.image 
                    ? <img src={product.image} className="w-full h-full object-cover group-hover:scale-110 transition duration-700" alt={product.name} /> 
                    : <span className="text-5xl">📦</span>
                  }
                  <div className="absolute top-4 right-4 bg-red-600 text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-tighter">
                    Limited
                  </div>
                </div>
                
                <h3 className="text-xl font-bold mb-1 group-hover:text-red-500 transition-colors duration-300">{product.name}</h3>
                <div className="flex justify-between items-center mt-4">
                  <p className="text-red-500 font-black text-2xl tracking-tighter">₹{product.price}</p>
                </div>
              </Link>
            </motion.div>
          ))}
        </AnimatePresence>
      </main>

      {/* EMPTY STATE */}
      {filtered.length === 0 && (
        <div className="text-center py-40">
          <div className="text-red-600 text-6xl mb-6 opacity-20 italic font-black">404</div>
          <p className="text-gray-500 text-2xl italic tracking-widest uppercase">No nexus artifacts found.</p>
          <button 
            onClick={() => { setSearch(""); setActiveCat("All"); }}
            className="mt-6 text-red-500 hover:underline font-bold"
          >
            Clear all filters
          </button>
        </div>
      )}

      <div className="h-20" />
    </div>
  );
}