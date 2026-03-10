"use client";
import React, { useState } from 'react';
import Link from 'next/link';
import { LayoutDashboard, Box, ShoppingCart, LogOut, Menu, X, Zap, KeyRound } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { usePathname, useRouter } from 'next/navigation';

const API = process.env.NEXT_PUBLIC_API_URL || "http://https://ecommerce-backend-pgyl.onrender.com";

export default function AdminLayout({ children }: { children: React.ReactNode }) {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [showPasswordModal, setShowPasswordModal] = useState(false);
  const [pwForm, setPwForm] = useState({ current: '', newPass: '', confirm: '' });
  const [pwError, setPwError] = useState('');
  const [pwSuccess, setPwSuccess] = useState('');

  const pathname = usePathname();
  const router = useRouter();

  const isLoginPage = pathname === "/admin/login";

  React.useEffect(() => {
    if (isLoginPage) return;
    const token   = localStorage.getItem("token");
    const isAdmin = localStorage.getItem("is_admin");
    if (!token || isAdmin !== "true") {
      router.replace("/admin/login");
    }
  }, [pathname]);

  const menuItems = [
    { name: 'Overview', icon: LayoutDashboard, path: '/admin' },
    { name: 'Products', icon: Box, path: '/admin/products' },
    { name: 'Orders', icon: ShoppingCart, path: '/admin/orders' },
  ];

  // ── Logout: token remove → login page ──
  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('is_admin');
    router.replace('/admin/login');
  };

  // ── Password Change ──
  const handlePasswordChange = async () => {
    setPwError('');
    setPwSuccess('');

    if (!pwForm.current || !pwForm.newPass || !pwForm.confirm) {
      setPwError('All fields are required.'); return;
    }
    if (pwForm.newPass !== pwForm.confirm) {
      setPwError('New passwords do not match.'); return;
    }
    if (pwForm.newPass.length < 4) {
      setPwError('Password must be at least 4 characters.'); return;
    }

    const token = localStorage.getItem('token');
    try {
      const res = await fetch(`${API}/api/stats/admin-change-password/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ current_password: pwForm.current, new_password: pwForm.newPass }),
      });
      const data = await res.json();
      if (res.ok) {
        setPwSuccess('Password changed! Please login again.');
        setTimeout(() => { setShowPasswordModal(false); handleLogout(); }, 1500);
      } else {
        setPwError(data.error || 'Failed to change password.');
      }
    } catch {
      setPwError('Network error.');
    }
  };

  if (isLoginPage) return <>{children}</>;

  return (
    <div className="min-h-screen bg-[#050505] text-white flex flex-col lg:flex-row font-sans">

      {/* --- MOBILE HEADER --- */}
      <div className="lg:hidden p-5 border-b border-white/10 flex justify-between items-center bg-black/50 backdrop-blur-md sticky top-0 z-50">
        <div className="flex items-center gap-2">
          <Zap className="text-indigo-500 fill-indigo-500" />
          <span className="font-black tracking-tighter text-xl">Bhatt Ji ADMIN</span>
        </div>
        <button onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}>
          {isMobileMenuOpen ? <X /> : <Menu />}
        </button>
      </div>

      {/* --- SIDEBAR (Desktop) --- */}
      <aside className="hidden lg:flex w-80 border-r border-white/10 flex-col p-8 gap-12 bg-white/2 backdrop-blur-3xl sticky top-0 h-screen">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-indigo-600 rounded-xl flex items-center justify-center shadow-lg shadow-indigo-500/20">
            <Zap className="w-6 h-6 text-white fill-white" />
          </div>
          <h1 className="text-2xl font-black tracking-tighter italic">BHATTJI<span className="text-indigo-600">.</span></h1>
        </div>

        <nav className="flex flex-col gap-3">
          {menuItems.map((item) => (
            <Link key={item.name} href={item.path} className="flex items-center gap-4 p-4 rounded-2xl hover:bg-white/5 transition-all group">
              <item.icon className="w-5 h-5 text-gray-500 group-hover:text-indigo-500 transition" />
              <span className="font-bold text-gray-400 group-hover:text-white transition">{item.name}</span>
            </Link>
          ))}
        </nav>

        <div className="mt-auto flex flex-col gap-2">
          {/* Change Password */}
          <button
            onClick={() => { setShowPasswordModal(true); setPwForm({ current: '', newPass: '', confirm: '' }); setPwError(''); setPwSuccess(''); }}
            className="flex items-center gap-4 p-4 text-gray-500 font-bold hover:bg-white/5 hover:text-white rounded-2xl transition"
          >
            <KeyRound className="w-5 h-5" /> Change Password
          </button>

          {/* Logout */}
          <button
            onClick={handleLogout}
            className="flex items-center gap-4 p-4 text-red-500 font-bold hover:bg-red-500/10 rounded-2xl transition"
          >
            <LogOut className="w-5 h-5" /> Exit to Store
          </button>
        </div>
      </aside>

      {/* --- MOBILE NAV OVERLAY --- */}
      <AnimatePresence>
        {isMobileMenuOpen && (
          <motion.div initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -20 }}
            className="lg:hidden bg-black border-b border-white/10 p-6 flex flex-col gap-4 fixed top-18.25 w-full z-40">
            {menuItems.map((item) => (
              <Link key={item.name} href={item.path} onClick={() => setIsMobileMenuOpen(false)} className="flex items-center gap-4 p-4 bg-white/5 rounded-xl">
                <item.icon className="w-5 h-5 text-indigo-500" />
                <span className="font-bold">{item.name}</span>
              </Link>
            ))}
            <button onClick={handleLogout} className="flex items-center gap-4 p-4 bg-red-500/10 text-red-400 rounded-xl font-bold">
              <LogOut className="w-5 h-5" /> Logout
            </button>
          </motion.div>
        )}
      </AnimatePresence>

      {/* --- MAIN CONTENT --- */}
      <main className="flex-1 p-6 lg:p-16 overflow-y-auto relative">
        <div className="absolute top-0 left-1/4 w-125 h-125 bg-indigo-600/5 rounded-full blur-[120px] pointer-events-none" />
        {children}
      </main>

      {/* ── Change Password Modal ── */}
      <AnimatePresence>
        {showPasswordModal && (
          <motion.div
            initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed inset-0 bg-black/70 backdrop-blur-sm z-200 flex items-center justify-center p-6"
            onClick={(e) => { if (e.target === e.currentTarget) setShowPasswordModal(false); }}
          >
            <motion.div
              initial={{ scale: 0.95, y: 20 }} animate={{ scale: 1, y: 0 }} exit={{ scale: 0.95, y: 20 }}
              className="bg-[#0f0f0f] border border-white/10 rounded-4xl p-8 w-full max-w-md shadow-2xl"
            >
              <div className="flex items-center justify-between mb-8">
                <h3 className="text-xl font-black flex items-center gap-2"><KeyRound className="w-5 h-5 text-indigo-400" /> Change Password</h3>
                <button onClick={() => setShowPasswordModal(false)} className="text-gray-600 hover:text-white transition"><X className="w-5 h-5" /></button>
              </div>

              <div className="space-y-4">
                <input
                  type="password" placeholder="Current Password"
                  value={pwForm.current} onChange={e => setPwForm({ ...pwForm, current: e.target.value })}
                  className="w-full bg-white/5 border border-white/10 rounded-2xl px-5 py-4 text-sm text-white placeholder-gray-600 outline-none focus:ring-2 focus:ring-indigo-500"
                />
                <input
                  type="password" placeholder="New Password"
                  value={pwForm.newPass} onChange={e => setPwForm({ ...pwForm, newPass: e.target.value })}
                  className="w-full bg-white/5 border border-white/10 rounded-2xl px-5 py-4 text-sm text-white placeholder-gray-600 outline-none focus:ring-2 focus:ring-indigo-500"
                />
                <input
                  type="password" placeholder="Confirm New Password"
                  value={pwForm.confirm} onChange={e => setPwForm({ ...pwForm, confirm: e.target.value })}
                  className="w-full bg-white/5 border border-white/10 rounded-2xl px-5 py-4 text-sm text-white placeholder-gray-600 outline-none focus:ring-2 focus:ring-indigo-500"
                />

                {pwError && <p className="text-red-400 text-xs font-bold px-1">{pwError}</p>}
                {pwSuccess && <p className="text-green-400 text-xs font-bold px-1">{pwSuccess}</p>}

                <button
                  onClick={handlePasswordChange}
                  className="w-full bg-indigo-600 hover:bg-indigo-700 py-4 rounded-2xl font-black text-sm transition mt-2"
                >
                  Update Password
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}