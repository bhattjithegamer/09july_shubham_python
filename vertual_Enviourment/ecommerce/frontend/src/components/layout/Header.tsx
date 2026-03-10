"use client";
import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { LogOut, UserCircle } from 'lucide-react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

const Header: React.FC = () => {
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
  const router = useRouter();

  useEffect(() => { setIsLoggedIn(!!localStorage.getItem('token')); }, []);

  const handleLogout = (): void => {
    localStorage.removeItem('token');
    setIsLoggedIn(false);
    router.push('/login');
  };

  return (
    <motion.nav
      initial={{ y: -20, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      className="sticky top-0 z-50 px-6 py-4"
      style={{ background: 'rgba(8,8,12,0.85)', borderBottom: '1px solid rgba(255,255,255,0.05)', backdropFilter: 'blur(24px)' }}
    >
      <div className="max-w-7xl mx-auto flex justify-between items-center">

        <Link href="/">
          <motion.h1
            whileHover={{ scale: 1.04 }}
            className="text-2xl font-black tracking-tighter cursor-pointer select-none"
            style={{ background: 'linear-gradient(90deg,#fff 0%,#a5b4fc 60%,#818cf8 100%)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}
          >
            BHATT JI <span style={{ WebkitTextFillColor: '#6366f1', fontStyle: 'italic' }}>STORE</span>
          </motion.h1>
        </Link>

        <AnimatePresence mode="wait">
          {isLoggedIn ? (
            <motion.div key="in" initial={{ opacity: 0, x: 10 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0 }} className="flex items-center space-x-4">
              <Link href="/profile" className="hidden sm:flex items-center space-x-2 text-sm font-bold text-gray-400 hover:text-white transition">
                <UserCircle className="w-5 h-5" /><span>Profile</span>
              </Link>
              <button
                onClick={handleLogout}
                className="flex items-center space-x-2 px-4 py-2 rounded-xl text-xs font-black uppercase tracking-widest transition-all"
                style={{ background: 'rgba(239,68,68,0.1)', border: '1px solid rgba(239,68,68,0.2)', color: '#f87171' }}
              >
                <LogOut className="w-3.5 h-3.5" /><span className="hidden sm:inline">Logout</span>
              </button>
            </motion.div>
          ) : (
            <motion.div key="out" initial={{ opacity: 0, x: 10 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0 }} className="flex items-center space-x-4">
              <Link href="/login" className="text-sm font-bold text-gray-400 hover:text-white transition">Login</Link>
              <Link href="/register"
                className="px-5 py-2 rounded-xl text-sm font-black uppercase tracking-widest text-white transition-all"
                style={{ background: 'linear-gradient(135deg,#4f46e5,#7c3aed)', boxShadow: '0 4px 20px rgba(99,102,241,0.3)' }}
              >
                Join
              </Link>
            </motion.div>
          )}
        </AnimatePresence>

      </div>
    </motion.nav>
  );
};

export default Header;