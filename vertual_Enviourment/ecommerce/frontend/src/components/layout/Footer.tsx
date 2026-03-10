"use client";
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Zap } from 'lucide-react';
import Link from 'next/link';

export default function Footer() {
  const [email, setEmail] = useState('');
  const [subscribed, setSubscribed] = useState(false);

  const handleSubscribe = (e: React.FormEvent) => {
    e.preventDefault();
    if (email) { setSubscribed(true); setEmail(''); }
  };

  const links = [
    { name: 'About Us', href: '/about' },
    { name: 'Shipping Policy', href: '/shipping' },
    { name: 'Terms & Conditions', href: '/terms' },
  ];

  const support = [
    { name: 'Help Center', href: '/help' },
    { name: 'Contact Support', href: '/contact' },
    { name: 'Returns', href: '/returns' },
  ];

  return (
    <footer className="relative bg-[#050505] text-white overflow-hidden">
      {/* Top Border Gradient - Changed to Red */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-200 h-px bg-linear-to-r from-transparent via-red-600/50 to-transparent" />
      
      <div className="relative max-w-7xl mx-auto px-6 pt-20 pb-10">
        <div className="grid grid-cols-1 lg:grid-cols-5 gap-12 mb-16">

          {/* Brand */}
          <div className="lg:col-span-2">
            <motion.div whileHover={{ scale: 1.02 }} className="inline-flex items-center gap-2 mb-6">
              {/* Icon Box - Changed to Red Gradient */}
              <div className="w-8 h-8 bg-linear-to-br from-red-600 to-red-900 rounded-lg flex items-center justify-center">
                <Zap className="w-4 h-4 text-white" />
              </div>
              <span className="text-xl font-black tracking-tighter bg-linear-to-r from-white to-red-500 bg-clip-text text-transparent uppercase">
                BHATT JI STORE
              </span>
            </motion.div>
            <p className="text-gray-500 text-sm leading-relaxed max-w-xs mb-8">
              Premium tech and lifestyle destination curated by Bhatt Ji. Experience quality like never before.
            </p>

            {/* Newsletter */}
            <div>
              <p className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-3">Stay in the loop</p>
              {subscribed ? (
                <p className="text-red-500 text-sm font-bold">You're subscribed!</p>
              ) : (
                <form onSubmit={handleSubscribe} className="flex gap-2">
                  <input type="email" value={email} onChange={(e) => setEmail(e.target.value)}
                    placeholder="your@email.com"
                    className="flex-1 bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-sm outline-none focus:ring-2 focus:ring-red-600/50 transition-all" />
                  <button type="submit" className="bg-red-600 hover:bg-red-700 transition-colors px-4 rounded-xl">
                    <ArrowRight className="w-4 h-4" />
                  </button>
                </form>
              )}
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <p className="text-xs font-black text-gray-400 uppercase tracking-[0.2em] mb-5">Quick Links</p>
            <ul className="space-y-3">
              {links.map((item) => (
                <li key={item.name}>
                  <Link href={item.href} className="text-gray-500 hover:text-white text-sm transition-colors flex items-center gap-2 group">
                    {/* Bullet - Changed to Red */}
                    <span className="w-1.5 h-1.5 rounded-full bg-red-600 opacity-0 group-hover:opacity-100 transition-all scale-0 group-hover:scale-100" />
                    {item.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Support */}
          <div>
            <p className="text-xs font-black text-gray-400 uppercase tracking-[0.2em] mb-5">Support</p>
            <ul className="space-y-3">
              {support.map((item) => (
                <li key={item.name}>
                  <Link href={item.href} className="text-gray-500 hover:text-white text-sm transition-colors flex items-center gap-2 group">
                    {/* Bullet - Changed to Red */}
                    <span className="w-1.5 h-1.5 rounded-full bg-red-600 opacity-0 group-hover:opacity-100 transition-all scale-0 group-hover:scale-100" />
                    {item.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="h-px bg-white/10 mb-8" />
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-gray-600 text-xs">
            © 2026 Bhatt Ji Store. <span className="text-red-600/50 ml-1">Developed by Bhatt Ji.</span>
          </p>
        </div>
      </div>
    </footer>
  );
}