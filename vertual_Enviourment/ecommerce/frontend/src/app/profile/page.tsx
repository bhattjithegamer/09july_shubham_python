"use client";
import React, { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { User, Mail, Settings, Check, X, Loader2, ShoppingBag, CheckCircle, Clock, Package, Trash2 } from "lucide-react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export default function ProfilePage() {
  const [user, setUser] = useState<any>(null);
  const [orders, setOrders] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({ first_name: "", username: "", email: "" });
  const [saving, setSaving] = useState(false);
  const [expandedOrder, setExpandedOrder] = useState<number | null>(null);

  useEffect(() => {
    fetchProfile();
    fetchOrders();
  }, []);

  const fetchProfile = async () => {
    const token = localStorage.getItem("token");
    if (!token) { window.location.href = "/login"; return; }
    try {
      const res = await fetch(`${API}/api/profile/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await res.json();
      if (res.ok) {
        setUser(data);
        setEditData({ first_name: data.first_name || "", username: data.username || "", email: data.email || "" });
      }
    } catch (err) { console.error(err); }
    finally { setLoading(false); }
  };

  const fetchOrders = async () => {
    const token = localStorage.getItem("token");
    if (!token) return;
    try {
      const res = await fetch(`${API}/api/orders/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await res.json();
      if (res.ok) setOrders(data);
    } catch (err) { console.error(err); }
  };

  const startEditing = () => {
    if (user) {
      setEditData({ first_name: user.first_name || "", username: user.username || "", email: user.email || "" });
      setIsEditing(true);
    }
  };

  const handleUpdate = async () => {
    setSaving(true);
    const token = localStorage.getItem("token");
    try {
      const res = await fetch(`${API}/api/profile/update/`, {
        method: "PUT",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
        body: JSON.stringify(editData),
      });
      if (res.ok) {
        await fetchProfile();
        setIsEditing(false);
        alert("Profile Updated Successfully!");
      } else {
        alert("Failed to update profile.");
      }
    } catch (err) { console.error(err); }
    finally { setSaving(false); }
  };

  const handleClearHistory = async () => {
    if (!confirm("Are you sure you want to delete all order history?")) return;
    const token = localStorage.getItem("token");
    try {
      const res = await fetch(`${API}/api/orders/clear/`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
      });
      if (res.ok) {
        setOrders([]);
        alert("Order history cleared!");
      } else {
        alert("Failed to clear history.");
      }
    } catch (err) { console.error(err); }
  };

  if (loading) return (
    <div className="text-center p-20 text-white font-bold animate-pulse">Loading Nexus Profile...</div>
  );

  return (
    <div className="min-h-screen bg-[#050505] text-white p-6 sm:p-12 font-sans relative">
      <div className="absolute top-0 right-0 w-125 h-125 bg-indigo-600/10 rounded-full blur-[150px]" />

      <div className="max-w-4xl mx-auto space-y-8">

        {/* --- PROFILE CARD --- */}
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}
          className="bg-white/5 backdrop-blur-3xl border border-white/10 p-10 rounded-[48px] shadow-2xl">
          <div className="flex justify-between items-start mb-10">
            <div className="flex items-center gap-6">
              <div className="w-24 h-24 bg-linear-to-br from-indigo-500 to-purple-600 rounded-3xl flex items-center justify-center shadow-xl shadow-indigo-500/20 text-5xl">👤</div>
              <div>
                <h2 className="text-3xl font-black">{user?.first_name || user?.username}</h2>
                <p className="text-gray-500 font-bold uppercase tracking-widest text-xs mt-1">Nexus Gold Member</p>
              </div>
            </div>
            {!isEditing ? (
              <button onClick={startEditing} className="p-4 bg-white/5 rounded-2xl hover:bg-white/10 transition">
                <Settings className="w-6 h-6 text-gray-400" />
              </button>
            ) : (
              <div className="flex gap-2">
                <button onClick={() => setIsEditing(false)} className="p-4 bg-red-500/10 text-red-500 rounded-2xl hover:bg-red-500/20 transition"><X /></button>
                <button onClick={handleUpdate} className="p-4 bg-green-500/10 text-green-500 rounded-2xl hover:bg-green-500/20 transition"><Check /></button>
              </div>
            )}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mt-10">
            <div className="space-y-2">
              <label className="text-xs font-bold text-gray-500 uppercase tracking-widest ml-1">Full Name</label>
              {isEditing ? (
                <input className="w-full bg-white/10 border border-white/20 p-4 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-white"
                  value={editData.first_name} onChange={(e) => setEditData({ ...editData, first_name: e.target.value })} />
              ) : (
                <div className="bg-white/5 p-4 rounded-2xl text-gray-300">{user?.first_name || "Not set"}</div>
              )}
            </div>
            <div className="space-y-2">
              <label className="text-xs font-bold text-gray-500 uppercase tracking-widest ml-1">Username</label>
              {isEditing ? (
                <input className="w-full bg-white/10 border border-white/20 p-4 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-white"
                  value={editData.username} onChange={(e) => setEditData({ ...editData, username: e.target.value })} />
              ) : (
                <div className="bg-white/5 p-4 rounded-2xl text-gray-300">{user?.username}</div>
              )}
            </div>
            <div className="space-y-2 md:col-span-2">
              <label className="text-xs font-bold text-gray-500 uppercase tracking-widest ml-1">Email Address</label>
              {isEditing ? (
                <input className="w-full bg-white/10 border border-white/20 p-4 rounded-2xl outline-none focus:ring-2 focus:ring-indigo-500 text-white"
                  value={editData.email} onChange={(e) => setEditData({ ...editData, email: e.target.value })} />
              ) : (
                <div className="bg-white/5 p-4 rounded-2xl flex items-center gap-3 text-gray-300">
                  <Mail className="w-4 h-4 text-gray-500" /> {user?.email}
                </div>
              )}
            </div>
          </div>

          {isEditing && (
            <motion.button whileTap={{ scale: 0.95 }} onClick={handleUpdate} disabled={saving}
              className="w-full mt-10 bg-indigo-600 py-4 rounded-2xl font-bold flex items-center justify-center gap-2 shadow-lg shadow-indigo-500/20 hover:bg-indigo-700 transition">
              {saving ? <Loader2 className="animate-spin" /> : "Save Changes"}
            </motion.button>
          )}
        </motion.div>

        {/* --- ORDERS CARD --- */}
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.1 }}
          className="bg-white/5 backdrop-blur-3xl border border-white/10 p-10 rounded-[48px] shadow-2xl">
          <div className="flex items-center gap-3 mb-8">
            <ShoppingBag className="w-6 h-6 text-indigo-400" />
            <h3 className="text-2xl font-black">My Orders</h3>
            <span className="ml-auto text-xs font-bold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 px-3 py-1 rounded-full">
              {orders.length} total
            </span>
            {orders.length > 0 && (
              <button
                onClick={handleClearHistory}
                className="flex items-center gap-1.5 text-xs font-bold bg-red-500/10 text-red-400 border border-red-500/20 px-3 py-1 rounded-full hover:bg-red-500/20 transition"
              >
                <Trash2 className="w-3 h-3" /> Delete History
              </button>
            )}
          </div>

          {orders.length === 0 ? (
            <div className="text-center py-12 text-gray-600">
              <ShoppingBag className="w-12 h-12 mx-auto mb-3 opacity-30" />
              <p className="font-bold">No orders yet</p>
            </div>
          ) : (
            <div className="space-y-4">
              {orders.map((order, i) => (
                <motion.div key={order.id} initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: i * 0.05 }}
                  className="bg-white/5 border border-white/10 rounded-2xl overflow-hidden">

                  {/* Order Row — click to expand */}
                  <div
                    className="flex items-center justify-between px-6 py-4 gap-4 cursor-pointer hover:bg-white/5 transition"
                    onClick={() => setExpandedOrder(expandedOrder === order.id ? null : order.id)}
                  >
                    {/* Products Summary */}
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2 mb-1">
                        <Package className="w-4 h-4 text-indigo-400 shrink-0" />
                        <p className="text-sm font-bold text-white truncate">
                          {order.items && order.items.length > 0
                            ? order.items.map((it: any) => `${it.name}${it.quantity > 1 ? ` ×${it.quantity}` : ''}`).join(', ')
                            : 'Order #' + order.id
                          }
                        </p>
                      </div>
                      <p className="text-xs text-gray-500 ml-6">{order.created_at}</p>
                    </div>

                    {/* Amount */}
                    <p className="text-lg font-black text-indigo-400 shrink-0">
                      ${parseFloat(order.total_amount).toFixed(2)}
                    </p>

                    {/* Status */}
                    {order.is_paid ? (
                      <span className="flex items-center gap-1.5 bg-green-500/10 text-green-400 border border-green-500/20 text-xs font-bold px-3 py-1.5 rounded-full shrink-0">
                        <CheckCircle className="w-3 h-3" /> Paid
                      </span>
                    ) : (
                      <span className="flex items-center gap-1.5 bg-yellow-500/10 text-yellow-400 border border-yellow-500/20 text-xs font-bold px-3 py-1.5 rounded-full shrink-0">
                        <Clock className="w-3 h-3" /> Pending
                      </span>
                    )}
                  </div>

                  {/* Expanded Detail */}
                  {expandedOrder === order.id && order.items && order.items.length > 0 && (
                    <div className="border-t border-white/10 px-6 py-4 space-y-2">
                      {order.items.map((item: any, idx: number) => (
                        <div key={idx} className="flex justify-between text-sm text-gray-400">
                          <span>{item.name} × {item.quantity}</span>
                          <span>${(parseFloat(item.price) * item.quantity).toFixed(2)}</span>
                        </div>
                      ))}
                      <div className="flex justify-between text-sm font-black text-white border-t border-white/10 pt-2 mt-2">
                        <span>Total</span>
                        <span>${parseFloat(order.total_amount).toFixed(2)}</span>
                      </div>
                    </div>
                  )}
                </motion.div>
              ))}
            </div>
          )}
        </motion.div>

      </div>
    </div>
  );
}