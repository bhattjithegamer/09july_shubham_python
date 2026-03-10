"use client";
import React from 'react';
import { HelpCircle, MessageCircle, ShieldCheck, Instagram } from 'lucide-react';

export default function HelpPage() {
  const faqs = [
    { q: "How do I track my order?", a: "Once shipped, you will receive a tracking link via email." },
    { q: "What payment methods do you accept?", a: "We accept all major credit cards, UPI, and Net Banking via Razorpay." },
    { q: "Is my data secure?", a: "Yes, we use industry-standard encryption to protect your information." }
  ];

  // લિંક્સ
  const whatsappUrl = "https://wa.me/918866440478"; // તમારો વોટ્સએપ નંબર
  const instagramUrl = "https://instagram.com/sanatani_bhatt_ji"; // તમારી ઈન્સ્ટા આઈડી

  return (
    <div className="min-h-screen bg-[#050505] text-white p-6 pt-32 pb-20">
      <div className="max-w-5xl mx-auto space-y-16">
        
        {/* Header */}
        <div className="text-center">
          <h1 className="text-6xl font-black text-indigo-500 tracking-tighter uppercase italic">Help Center</h1>
          <p className="text-gray-500 mt-4 uppercase tracking-[0.3em] text-xs font-bold">Bhatt Ji Support System</p>
        </div>

        {/* Support Cards Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          
          {/* FAQ Card */}
          <div className="bg-white/5 p-8 rounded-4xl border border-white/10 text-center hover:bg-white/8 transition-all">
            <HelpCircle className="mx-auto mb-4 text-indigo-400 w-10 h-10" />
            <h3 className="font-black uppercase tracking-widest text-sm">FAQs</h3>
            <p className="text-gray-500 text-[10px] mt-2">Common Questions</p>
          </div>

          {/* WhatsApp Chat Card */}
          <a 
            href={whatsappUrl} 
            target="_blank" 
            rel="noopener noreferrer"
            className="bg-white/5 p-8 rounded-4xl border border-white/10 text-center hover:border-green-500/50 hover:bg-green-500/5 transition-all group"
          >
            <MessageCircle className="mx-auto mb-4 text-green-400 w-10 h-10 group-hover:scale-110 transition-transform" />
            <h3 className="font-black uppercase tracking-widest text-sm text-white">Chat with Us</h3>
            <p className="text-green-500/70 text-[10px] mt-2 font-bold uppercase">Open WhatsApp</p>
          </a>

          {/* Instagram Card */}
          <a 
            href={instagramUrl} 
            target="_blank" 
            rel="noopener noreferrer"
            className="bg-white/5 p-8 rounded-4xl border border-white/10 text-center hover:border-pink-500/50 hover:bg-pink-500/5 transition-all group"
          >
            <Instagram className="mx-auto mb-4 text-pink-500 w-10 h-10 group-hover:scale-110 transition-transform" />
            <h3 className="font-black uppercase tracking-widest text-sm text-white">Instagram</h3>
            <p className="text-pink-500/70 text-[10px] mt-2 font-bold uppercase">Follow Bhatt Ji</p>
          </a>

          {/* Security Card */}
          <div className="bg-white/5 p-8 rounded-4xl border border-white/10 text-center hover:bg-white/8 transition-all">
            <ShieldCheck className="mx-auto mb-4 text-purple-400 w-10 h-10" />
            <h3 className="font-black uppercase tracking-widest text-sm">Security</h3>
            <p className="text-gray-500 text-[10px] mt-2">100% Safe Payments</p>
          </div>

        </div>

        {/* FAQs Section */}
        <div className="space-y-6 bg-white/5 p-10 rounded-[40px] border border-white/10 backdrop-blur-md">
          <h2 className="text-2xl font-black uppercase tracking-widest mb-8 flex items-center gap-4">
            <div className="w-8 h-0.5 bg-indigo-500"></div>
            Frequently Asked Questions
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {faqs.map((f, i) => (
              <div key={i} className="bg-white/5 p-6 rounded-3xl border border-white/5 hover:border-white/20 transition-all">
                <h4 className="font-bold text-white mb-2 text-sm uppercase tracking-wide">{f.q}</h4>
                <p className="text-gray-500 text-xs leading-relaxed">{f.a}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Bottom Credit Line */}
        <div className="text-center pt-10 border-t border-white/5">
          <p className="text-gray-700 text-[10px] tracking-[0.5em] uppercase font-black">
            Support managed by <span className="text-indigo-500">Bhatt Ji</span>
          </p>
        </div>

      </div>
    </div>
  );
}