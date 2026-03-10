"use client";
import React from 'react';
import { Mail, Phone, MapPin } from 'lucide-react';

export default function ContactPage() {
  return (
    <div className="min-h-screen bg-black text-white p-10 pt-32">
      <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-20">
        <div>
          <h1 className="text-6xl font-black uppercase mb-8">Get In <span className="text-indigo-500">Touch</span></h1>
          <div className="space-y-8">
            <div className="flex items-center gap-6">
              <div className="w-14 h-14 bg-indigo-600/20 rounded-2xl flex items-center justify-center"><Mail className="text-indigo-400" /></div>
              <div><p className="text-gray-500 text-xs uppercase font-bold">Email Us</p><p className="font-bold">bhattbhudev84.com</p></div>
            </div>
            <div className="flex items-center gap-6">
              <div className="w-14 h-14 bg-green-600/20 rounded-2xl flex items-center justify-center"><Phone className="text-green-400" /></div>
              <div><p className="text-gray-500 text-xs uppercase font-bold">Call Us</p><p className="font-bold">+91 88664 40478</p></div>
            </div>
          </div>
        </div>
        <div className="bg-white/5 p-10 rounded-[40px] border border-white/10">
          <form className="space-y-6">
            <input placeholder="Your Name" className="w-full bg-white/5 border border-white/10 p-4 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500" />
            <input placeholder="Email Address" className="w-full bg-white/5 border border-white/10 p-4 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500" />
            <textarea placeholder="How can we help?" className="w-full bg-white/5 border border-white/10 p-4 rounded-2xl h-40 outline-none focus:ring-2 focus:ring-indigo-500 resize-none" />
            <button className="w-full bg-indigo-600 py-4 rounded-2xl font-black uppercase tracking-widest hover:bg-indigo-700 transition">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  );
}