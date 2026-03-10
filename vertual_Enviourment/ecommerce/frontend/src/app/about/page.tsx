"use client";
import React from 'react';
import { motion } from 'framer-motion';

export default function AboutPage() {
  return (
    <div className="min-h-screen bg-[#020202] text-white p-6 pt-32 pb-20">
      <div className="max-w-6xl mx-auto">
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          
          {/* Left Side: Photo with Proper Zoom-out */}
          <motion.div 
            initial={{ opacity: 0, scale: 0.9 }} 
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8 }}
            className="relative group mx-auto lg:mx-0 w-full max-w-100" // કન્ટેનર નાનું કર્યું જેથી ઝૂમ આઉટ લાગે
          >
            {/* Background Glow */}
            <div className="absolute -inset-4 bg-indigo-500/20 rounded-[50px] blur-3xl opacity-30 group-hover:opacity-50 transition duration-1000"></div>
            
            <div className="relative h-125 w-full overflow-hidden rounded-[40px] border border-white/10 shadow-2xl bg-black">
              <img 
                src="/me.jpg" 
                alt="Sanatani Bhatt Ji"
                // object-cover સાથે h-full રાખ્યું છે પણ કન્ટેનરની સાઈઝ નાની કરી છે
                className="w-full h-full object-cover object-top transition duration-700 group-hover:scale-105"
                style={{ 
                  filter: 'contrast(1.15) brightness(1.05) saturate(1.2)', // કલર્સ શાર્પ કરવા માટે
                  imageRendering: 'auto'
                }}
              />
            </div>
            
            {/* Floating Badge */}
            
          </motion.div>

          {/* Right Side: Content */}
          <motion.div 
            initial={{ opacity: 0, x: 40 }} 
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            className="space-y-8"
          >
            <div>
              <h1 className="text-7xl font-black tracking-tighter uppercase leading-none">
                ABOUT <span className="text-indigo-500 italic">BHATT JI</span>
              </h1>
              <div className="flex items-center gap-3 mt-4">
                <div className="h-px w-16 bg-indigo-500/50"></div>
                <p className="text-gray-500 font-bold uppercase tracking-[0.4em] text-[10px]">
                  The Architect of Excellence
                </p>
              </div>
            </div>

            <p className="text-gray-400 text-lg leading-relaxed font-medium max-w-xl">
              I am <span className="text-white font-bold">Shubham Bhatt </span>. 
              Everything you see here is a reflection of my passion for technology and premium design. 
              I believe that a digital store shouldn't just sell products; it should provide an experience 
              that stays with you.
            </p>

            <div className="space-y-4">
              <div className="flex items-start gap-4 p-4 rounded-3xl bg-white/5 border border-white/5 hover:bg-white/8 transition-all group">
                <div className="w-10 h-10 rounded-2xl bg-indigo-500/20 flex items-center justify-center text-indigo-400 font-black group-hover:bg-indigo-500 group-hover:text-white transition-all">01</div>
                <div>
                  <h4 className="font-bold text-white uppercase text-sm">Unmatched Quality</h4>
                  <p className="text-gray-500 text-xs mt-1">Handpicked premium products curated for the elite.</p>
                </div>
              </div>
              <div className="flex items-start gap-4 p-4 rounded-3xl bg-white/5 border border-white/5 hover:bg-white/8 transition-all group">
                <div className="w-10 h-10 rounded-2xl bg-purple-500/20 flex items-center justify-center text-purple-400 font-black group-hover:bg-purple-500 group-hover:text-white transition-all">02</div>
                <div>
                  <h4 className="font-bold text-white uppercase text-sm">Secure Shopping</h4>
                  <p className="text-gray-500 text-xs mt-1">End-to-end encryption for your peace of mind.</p>
                </div>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Footer Credit Line */}
        <motion.div 
          initial={{ opacity: 0 }} 
          animate={{ opacity: 1 }} 
          transition={{ delay: 1 }}
          className="mt-32 pt-10 border-t border-white/5 text-center"
        >
          <p className="text-gray-700 text-[10px] tracking-[0.5em] uppercase font-black">
            This website was developed by <span className="text-indigo-500">Sanatani Bhatt Ji</span>
          </p>
        </motion.div>

      </div>
    </div>
  );
}