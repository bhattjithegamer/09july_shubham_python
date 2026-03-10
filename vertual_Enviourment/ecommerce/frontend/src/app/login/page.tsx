"use client";

/**
 * NEXUS STORE - ADVANCED LOGIN PAGE
 * Features: Framer Motion Animations, Google OAuth, JWT Integration, Glassmorphism UI
 */

import React, { useState } from "react";
import { motion } from "framer-motion";
import { LogIn, Mail, Lock, ArrowRight } from "lucide-react";
import Link from "next/link";
import { GoogleOAuthProvider, GoogleLogin } from '@react-oauth/google';

// Environment variables માંથી વેલ્યુ લીધી
const API = process.env.NEXT_PUBLIC_API_URL;
const GOOGLE_CLIENT_ID = process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID || "";

// Helper: token cookie માં save કરો (middleware વાંચી શકે)
function saveTokenToCookie(token: string) {
  document.cookie = `token=${token}; path=/; max-age=${60 * 60 * 24 * 7}`; // 7 days
}

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const response = await fetch(`${API}/api/login/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem("token", data.access);
        localStorage.setItem("refresh_token", data.refresh);
        localStorage.setItem("username", username);
        saveTokenToCookie(data.access); // ← Middleware માટે cookie

        const params = new URLSearchParams(window.location.search);
        const next = params.get("next") || "/";
        window.location.href = next;
      } else {
        alert("Authentication Failed: Please check your credentials.");
      }
    } catch (error) {
      console.error("Login request failed:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleGoogleSuccess = async (credentialResponse: any) => {
    const googleToken = credentialResponse.credential;
    try {
      const res = await fetch(`${API}/api/google-login/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token: googleToken }),
      });

      const data = await res.json();

      if (res.ok) {
        localStorage.setItem("token", data.tokens.access);
        localStorage.setItem("username", data.user.email.split("@")[0]);
        saveTokenToCookie(data.tokens.access); // ← Middleware માટે cookie

        const params = new URLSearchParams(window.location.search);
        const next = params.get("next") || "/";
        window.location.href = next;
      } else {
        alert("Google Verification Failed on Server.");
      }
    } catch (error) {
      console.error("Google login error:", error);
    }
  };

  return (
    <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
      <div className="min-h-screen flex items-center justify-center bg-[#050505] relative overflow-hidden p-6 font-sans">

        <div className="absolute top-[-20%] left-[-10%] w-150 h-150 bg-blue-600/20 rounded-full blur-[150px] animate-pulse" />
        <div className="absolute bottom-[-20%] right-[-10%] w-150 h-150 bg-purple-600/20 rounded-full blur-[150px] animate-pulse delay-1000" />

        <motion.div
          initial={{ opacity: 0, scale: 0.9, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="w-full max-w-md z-10"
        >
          <div className="bg-white/5 backdrop-blur-3xl border border-white/10 p-10 rounded-[48px] shadow-[0_25px_50px_-12px_rgba(0,0,0,0.5)]">

            <div className="text-center mb-10">
              <motion.div
                whileHover={{ rotate: 10, scale: 1.1 }}
                className="inline-block p-4 bg-linear-to-br from-blue-500 to-indigo-600 rounded-3xl mb-4 shadow-xl shadow-blue-500/20"
              >
                <LogIn className="w-8 h-8 text-white" />
              </motion.div>
              <h2 className="text-3xl font-black text-white tracking-tight leading-tight">Welcome to Nexus</h2>
              <p className="text-gray-400 mt-2 text-sm font-medium">Elevate your shopping experience</p>
            </div>

            <form onSubmit={handleLogin} className="space-y-5">
              <div className="relative group">
                <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500 group-focus-within:text-blue-500 transition-colors" />
                <input
                  type="text"
                  placeholder="Username or Email"
                  className="w-full bg-white/5 border border-white/10 p-4 pl-12 rounded-2xl text-white outline-none focus:ring-2 focus:ring-blue-500/50 transition-all placeholder:text-gray-600"
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
              </div>

              <div className="relative group">
                <Lock className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500 group-focus-within:text-purple-500 transition-colors" />
                <input
                  type="password"
                  placeholder="Password"
                  className="w-full bg-white/5 border border-white/10 p-4 pl-12 rounded-2xl text-white outline-none focus:ring-2 focus:ring-purple-500/50 transition-all placeholder:text-gray-600"
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>

              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                disabled={isLoading}
                className="w-full bg-linear-to-r from-blue-600 to-indigo-600 text-white py-4 rounded-2xl font-bold flex items-center justify-center gap-2 shadow-lg shadow-blue-600/20 disabled:opacity-50"
              >
                {isLoading ? "Authenticating..." : "Sign In"} <ArrowRight className="w-5 h-5" />
              </motion.button>
            </form>

            <div className="flex items-center my-8 gap-4 px-2">
              <div className="h-px bg-white/10 flex-1" />
              <span className="text-gray-500 text-[10px] font-black uppercase tracking-[0.2em]">or explore with</span>
              <div className="h-px bg-white/10 flex-1" />
            </div>

            <div className="flex flex-col items-center justify-center space-y-4">
              <div className="w-full overflow-hidden rounded-full flex justify-center">
                <GoogleLogin
                  onSuccess={handleGoogleSuccess}
                  onError={() => console.log('Login Failed')}
                  theme="filled_black"
                  shape="pill"
                  size="large"
                  text="signin_with"
                  width="320px"
                />
              </div>
            </div>

            <p className="mt-10 text-center text-gray-500 text-sm font-medium">
              New to Nexus?
              <Link href="/register" className="text-blue-400 font-bold ml-1.5 hover:text-blue-300 transition-colors underline-offset-4 hover:underline">
                Create Account
              </Link>
            </p>
          </div>
        </motion.div>
      </div>
    </GoogleOAuthProvider>
  );
}