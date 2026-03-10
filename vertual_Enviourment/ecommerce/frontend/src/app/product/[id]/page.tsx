"use client";
import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { Package } from 'lucide-react';

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

const getImageUrl = (image: string | null | undefined): string | null => {
  if (!image) return null;
  if (image.startsWith("http://") || image.startsWith("https://")) return image;
  return `${API}${image.startsWith("/") ? "" : "/"}${image}`;
};

interface Product {
  id: number;
  name: string;
  category: string;
  price: string;
  description: string;
  image?: string | null;
}

export default function AdminProducts() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchProducts = async () => {
    const res = await fetch(`${API}/api/stats/products/`);
    const data = await res.json();
    setProducts(data);
    setLoading(false);
  };

  useEffect(() => { fetchProducts(); }, []);

  return (
    <div className="relative z-10 space-y-10">
      <header>
        <h2 className="text-4xl font-black tracking-tight">Products</h2>
      </header>

      {loading ? (
        <div className="space-y-4">
          {[1, 2, 3].map(i => <div key={i} className="h-16 bg-white/5 rounded-2xl animate-pulse" />)}
        </div>
      ) : (
        <div className="bg-white/5 border border-white/10 rounded-[40px] overflow-hidden">
          <table className="w-full text-left">
            <thead>
              <tr className="text-gray-500 text-[10px] font-black uppercase tracking-[0.2em] border-b border-white/5">
                <th className="px-8 py-5">Product</th>
                <th className="px-8 py-5 hidden sm:table-cell">Category</th>
                <th className="px-8 py-5">Price</th>
                <th className="px-8 py-5 hidden md:table-cell">Description</th>
              </tr>
            </thead>
            <tbody>
              {products.map((p, i) => (
                <motion.tr
                  key={p.id}
                  initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.04 }}
                  className="border-b border-white/5 hover:bg-white/2 transition"
                >
                  <td className="px-8 py-5">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-indigo-500/10 rounded-xl flex items-center justify-center overflow-hidden shrink-0">
                        {getImageUrl(p.image) ? (
                          <img src={getImageUrl(p.image)!} alt={p.name} className="w-full h-full object-cover" />
                        ) : (
                          <Package className="w-4 h-4 text-indigo-400" />
                        )}
                      </div>
                      <span className="font-bold text-sm">{p.name}</span>
                    </div>
                  </td>
                  <td className="px-8 py-5 hidden sm:table-cell">
                    <span className="text-xs font-bold px-3 py-1 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
                      {p.category || '—'}
                    </span>
                  </td>
                  <td className="px-8 py-5 font-black text-indigo-400">₹{p.price}</td>
                  <td className="px-8 py-5 text-gray-500 text-sm hidden md:table-cell max-w-xs truncate">{p.description}</td>
                </motion.tr>
              ))}
            </tbody>
          </table>

          {products.length === 0 && (
            <div className="text-center py-16 text-gray-600">
              <Package className="w-10 h-10 mx-auto mb-3 opacity-30" />
              <p className="font-bold text-sm">No products yet</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}