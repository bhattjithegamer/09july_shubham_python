"use client";
import React, { useState } from "react";
import { motion, AnimatePresence } from "framer-motion"; // એનિમેશન માટે
import { UserPlus, Mail, Lock, User, ArrowRight, AlertCircle } from "lucide-react";
import Link from "next/link";
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';

// Environment variables માંથી વેલ્યુ લોડ કરી
const API = process.env.NEXT_PUBLIC_API_URL;
const GOOGLE_CLIENT_ID = process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID || "";

export default function RegisterPage() {
  const [formData, setFormData] = useState({ username: "", email: "", password: "" });
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState(""); // Inline Error State

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setErrorMsg(""); // Clear old errors

    try {
      // હાર્ડકોડેડ URL ની જગ્યાએ API વેરીએબલ વાપર્યો
      const res = await fetch(`${API}/api/register/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await res.json();

      if (res.ok) {
        localStorage.setItem("token", data.tokens.access);
        window.location.href = "/"; // Success: Direct redirect to home
      } else {
        // Show the error from backend in our UI
        setErrorMsg(data.error || "Something went wrong. Try again.");
      }
    } catch (err) {
      setErrorMsg("Connection failed. Check if Backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
      <div className="min-h-screen flex items-center justify-center bg-[#050505] p-6 text-white overflow-hidden relative font-sans">
        
        {/* Decorative Background */}
        <div className="absolute top-[-10%] right-[-10%] w-125 h-125 bg-indigo-600/10 rounded-full blur-[120px]"></div>

        <motion.div 
          initial={{ opacity: 0, y: 20 }} 
          animate={{ opacity: 1, y: 0 }} 
          className="w-full max-w-md z-10"
        >
          <div className="bg-white/5 backdrop-blur-3xl border border-white/10 p-10 rounded-[48px] shadow-2xl">
            
            <div className="text-center mb-8">
              <h2 className="text-3xl font-black mb-2 tracking-tight">Join Nexus</h2>
              <p className="text-gray-400 text-sm font-medium">Create your premium account</p>
            </div>

            {/* --- INLINE ERROR MESSAGE --- */}
            <AnimatePresence>
              {errorMsg && (
                <motion.div 
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  exit={{ opacity: 0, height: 0 }}
                  className="bg-red-500/10 border border-red-500/50 p-4 rounded-2xl mb-6 flex items-center gap-3 text-red-400 text-sm overflow-hidden"
                >
                  <AlertCircle className="w-5 h-5 shrink-0" />
                  <p>{errorMsg}</p>
                </motion.div>
              )}
            </AnimatePresence>

            <form onSubmit={handleRegister} className="space-y-4">
              {/* Username Input */}
              <div className="relative group">
                <User className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500 group-focus-within:text-indigo-500 transition-colors" />
                <input 
                  type="text" placeholder="Username" required
                  className="w-full bg-white/5 border border-white/10 p-4 pl-12 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all placeholder:text-gray-600"
                  onChange={(e) => setFormData({...formData, username: e.target.value})}
                />
              </div>

              {/* Email Input */}
              <div className="relative group">
                <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500 group-focus-within:text-indigo-500 transition-colors" />
                <input 
                  type="email" placeholder="Email" required
                  className="w-full bg-white/5 border border-white/10 p-4 pl-12 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all placeholder:text-gray-600"
                  onChange={(e) => setFormData({...formData, email: e.target.value})}
                />
              </div>

              {/* Password Input */}
              <div className="relative group">
                <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500 group-focus-within:text-indigo-500 transition-colors" />
                <input 
                  type="password" placeholder="Password" required
                  className="w-full bg-white/5 border border-white/10 p-4 pl-12 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500/50 transition-all placeholder:text-gray-600"
                  onChange={(e) => setFormData({...formData, password: e.target.value})}
                />
              </div>

              <motion.button 
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                disabled={loading} 
                className="w-full bg-indigo-600 hover:bg-indigo-700 py-4 rounded-2xl font-bold flex items-center justify-center gap-2 transition-all shadow-lg shadow-indigo-600/20 disabled:opacity-50"
              >
                {loading ? "Creating account..." : "Sign Up"} <ArrowRight className="w-5 h-5" />
              </motion.button>
            </form>

            <div className="my-8 flex items-center gap-4">
              <div className="h-px bg-white/10 flex-1"></div>
              <span className="text-gray-500 text-[10px] font-bold uppercase tracking-widest">or Join with</span>
              <div className="h-px bg-white/10 flex-1"></div>
            </div>

            <div className="flex justify-center">
              <GoogleLogin 
                onSuccess={() => (window.location.href = "/")} 
                onError={() => setErrorMsg("Google Registration Failed")}
                theme="filled_black" 
                shape="pill" 
                width="320px"
              />
            </div>

            <p className="mt-8 text-center text-sm text-gray-400 font-medium">
              Already a member? 
              <Link href="/login" className="text-indigo-400 font-bold hover:text-indigo-300 ml-1.5 transition-colors underline-offset-4 hover:underline">
                Login
              </Link>
            </p>
          </div>
        </motion.div>
      </div>
    </GoogleOAuthProvider>
  );
}