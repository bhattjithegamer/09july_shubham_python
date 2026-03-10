"use client";
import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ShieldCheck, Eye, EyeOff, Lock, User, AlertTriangle } from "lucide-react";
import { useRouter } from "next/navigation";

const API = process.env.NEXT_PUBLIC_API_URL || "https://ecommerce-backend-pgyl.onrender.com";

export default function AdminLoginPage() {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPass, setShowPass] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [shake, setShake] = useState(false);

  // Already logged in as admin → redirect
  useEffect(() => {
    const isAdmin = localStorage.getItem("is_admin");
    if (isAdmin === "true") router.replace("/admin");
  }, []);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await fetch(`${API}/api/stats/admin-login/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();

      if (res.ok && data.is_admin) {
        localStorage.setItem("token", data.access);
        localStorage.setItem("is_admin", "true");
        router.replace("/admin");
      } else {
        setError(data.error || "Access denied. Admins only.");
        triggerShake();
      }
    } catch {
      setError("Connection failed. Try again.");
      triggerShake();
    } finally {
      setLoading(false);
    }
  };

  const triggerShake = () => {
    setShake(true);
    setTimeout(() => setShake(false), 600);
  };

  return (
    <div className="min-h-screen bg-[#030303] flex items-center justify-center p-6 relative overflow-hidden">

      {/* Background glow */}
      <div className="absolute inset-0 pointer-events-none">
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-150 h-150 bg-red-600/5 rounded-full blur-[120px]" />
        <div className="absolute top-1/4 right-1/4 w-75 h-75 bg-indigo-600/5 rounded-full blur-[100px]" />
        {/* Grid lines */}
        <div className="absolute inset-0 opacity-[0.03]"
          style={{ backgroundImage: 'linear-gradient(#fff 1px, transparent 1px), linear-gradient(90deg, #fff 1px, transparent 1px)', backgroundSize: '60px 60px' }} />
      </div>

      <motion.div
        initial={{ opacity: 0, y: 32, scale: 0.97 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
        className="w-full max-w-md relative z-10"
      >
        {/* Card */}
        <motion.div
          animate={shake ? { x: [-8, 8, -6, 6, -3, 3, 0] } : { x: 0 }}
          transition={{ duration: 0.5 }}
          className="bg-white/3 border border-white/10 rounded-[40px] p-10 backdrop-blur-2xl shadow-2xl"
        >
          {/* Icon */}
          <div className="flex justify-center mb-8">
            <div className="relative">
              <div className="w-20 h-20 bg-red-500/10 border border-red-500/20 rounded-3xl flex items-center justify-center shadow-xl shadow-red-500/10">
                <ShieldCheck className="w-10 h-10 text-red-400" />
              </div>
              <div className="absolute -top-1 -right-1 w-4 h-4 bg-red-500 rounded-full border-2 border-[#030303]" />
            </div>
          </div>

          {/* Title */}
          <div className="text-center mb-10">
            <h1 className="text-3xl font-black tracking-tight text-white">Admin Portal</h1>
            <p className="text-gray-600 text-xs uppercase tracking-[0.25em] font-bold mt-2">Restricted Access Only</p>
          </div>

          {/* Error */}
          <AnimatePresence>
            {error && (
              <motion.div
                initial={{ opacity: 0, y: -8, height: 0 }}
                animate={{ opacity: 1, y: 0, height: "auto" }}
                exit={{ opacity: 0, height: 0 }}
                className="flex items-center gap-3 bg-red-500/10 border border-red-500/20 text-red-400 rounded-2xl px-4 py-3 mb-6 text-sm font-bold"
              >
                <AlertTriangle className="w-4 h-4 shrink-0" />
                {error}
              </motion.div>
            )}
          </AnimatePresence>

          {/* Form */}
          <form onSubmit={handleLogin} className="space-y-4">
            {/* Username */}
            <div className="relative">
              <User className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-600 pointer-events-none" />
              <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={e => setUsername(e.target.value)}
                required
                autoComplete="username"
                className="w-full bg-white/5 border border-white/10 rounded-2xl pl-11 pr-4 py-4 text-sm text-white placeholder-gray-600 outline-none focus:ring-2 focus:ring-red-500/50 focus:border-red-500/30 transition"
              />
            </div>

            {/* Password */}
            <div className="relative">
              <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-600 pointer-events-none" />
              <input
                type={showPass ? "text" : "password"}
                placeholder="Password"
                value={password}
                onChange={e => setPassword(e.target.value)}
                required
                autoComplete="current-password"
                className="w-full bg-white/5 border border-white/10 rounded-2xl pl-11 pr-12 py-4 text-sm text-white placeholder-gray-600 outline-none focus:ring-2 focus:ring-red-500/50 focus:border-red-500/30 transition"
              />
              <button
                type="button"
                onClick={() => setShowPass(!showPass)}
                className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-600 hover:text-gray-400 transition"
              >
                {showPass ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
              </button>
            </div>

            {/* Submit */}
            <motion.button
              whileTap={{ scale: 0.97 }}
              type="submit"
              disabled={loading}
              className="w-full mt-2 bg-red-600 hover:bg-red-700 disabled:opacity-50 disabled:cursor-not-allowed text-white py-4 rounded-2xl font-black text-sm uppercase tracking-widest transition flex items-center justify-center gap-2 shadow-lg shadow-red-600/20"
            >
              {loading ? (
                <svg className="w-5 h-5 animate-spin" viewBox="0 0 24 24" fill="none">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"/>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
                </svg>
              ) : (
                <><ShieldCheck className="w-4 h-4" /> Authenticate</>
              )}
            </motion.button>
          </form>

          {/* Footer */}
          <p className="text-center text-gray-700 text-[10px] uppercase tracking-widest font-bold mt-8">
            Unauthorized access is prohibited
          </p>
        </motion.div>
      </motion.div>
    </div>
  );
}