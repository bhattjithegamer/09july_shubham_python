"use client";
import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { DollarSign, Package, ShoppingBasket, CheckCircle, Flame } from 'lucide-react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell
} from 'recharts';

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

const CustomTooltip = ({ active, payload, label }: any) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-[#0f0f0f] border border-white/10 rounded-2xl px-5 py-3 shadow-2xl">
        <p className="text-[10px] text-gray-500 uppercase tracking-widest font-black mb-1">{label}</p>
        <p className="text-white font-black text-lg">
          {payload[0].value} <span className="text-xs text-gray-500 font-bold">sold</span>
        </p>
      </div>
    );
  }
  return null;
};

const BAR_COLORS = [
  '#6366f1','#8b5cf6','#a78bfa','#818cf8','#c4b5fd',
  '#7c3aed','#4f46e5','#6d28d9','#5b21b6','#4338ca',
];

export default function AdminDashboard() {
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const token = localStorage.getItem("token");
        const res = await fetch(`${API}/api/stats/stats/`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        const data = await res.json();
        setStats(data);
      } catch (err) {
        console.error("Stats fetch error:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  const cards = [
    { title: "Total Revenue", value: `$${stats?.sales?.toLocaleString() || 0}`, icon: DollarSign, color: "text-green-400", bg: "bg-green-400/10" },
    { title: "Total Orders",  value: stats?.orders  || 0, icon: ShoppingBasket, color: "text-indigo-400", bg: "bg-indigo-400/10" },
    { title: "Inventory",     value: stats?.products || 0, icon: Package,       color: "text-purple-400", bg: "bg-purple-400/10" },
  ];

  const paidOrders = stats?.recent_orders?.filter((o: any) => o.is_paid === true) || [];

  // top_products — backend must return: [{ name, sold }]
  const topProducts: { name: string; sold: number }[] =
    (stats?.top_products || []).slice(0, 10).map((p: any) => ({
      name: p.name || p.product__name || 'Unknown',
      sold: p.sold || p.total_sold || p.quantity || 0,
    }));

  if (loading) return (
    <div className="h-screen flex items-center justify-center text-white font-black tracking-widest uppercase animate-pulse">
      Loading Dashboard...
    </div>
  );

  return (
    <div className="relative z-10 space-y-12 p-6">
      <header>
        <h2 className="text-5xl font-black tracking-tight text-white uppercase">System Overview</h2>
        <p className="text-gray-500 font-medium mt-3 uppercase tracking-widest text-xs">Store Management Cloud</p>
      </header>

      {/* STATS GRID */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {cards.map((card, i) => (
          <motion.div
            key={card.title}
            initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.1 }}
            className="bg-white/5 border border-white/10 p-8 rounded-[40px] shadow-2xl backdrop-blur-md hover:bg-white/8 transition-all"
          >
            <div className={`w-14 h-14 ${card.bg} ${card.color} rounded-2xl flex items-center justify-center mb-8 shadow-inner`}>
              <card.icon className="w-7 h-7" />
            </div>
            <p className="text-gray-500 text-[10px] font-black uppercase tracking-widest">{card.title}</p>
            <h3 className="text-4xl font-black mt-2 tracking-tighter text-white">{card.value}</h3>
          </motion.div>
        ))}
      </div>

      {/* ── TOP PRODUCTS CHART ── */}
      <motion.div
        initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.35 }}
        className="bg-white/5 border border-white/10 rounded-[48px] p-10 shadow-2xl backdrop-blur-lg"
      >
        <div className="flex items-center justify-between mb-10 flex-wrap gap-4">
          <div className="flex items-center gap-4">
            <div className="w-12 h-12 bg-orange-500/10 rounded-2xl flex items-center justify-center">
              <Flame className="w-6 h-6 text-orange-400" />
            </div>
            <div>
              <h3 className="text-2xl font-black tracking-tight text-white uppercase">Top Products</h3>
              <p className="text-gray-600 text-[10px] uppercase tracking-widest font-bold mt-0.5">By units sold</p>
            </div>
          </div>
          <span className="text-xs font-bold text-gray-500 bg-white/5 px-4 py-2 rounded-full border border-white/10">
            Top {topProducts.length} products
          </span>
        </div>

        {topProducts.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-20 text-gray-700">
            <Package className="w-14 h-14 mb-4 opacity-20" />
            <p className="font-black uppercase tracking-widest text-sm">No product data</p>
            <p className="text-xs mt-2 text-gray-600 text-center">
              Backend API માં{' '}
              <code className="bg-white/5 px-2 py-0.5 rounded-lg text-indigo-400">top_products</code>
              {' '}field add કરો — નીચે જુઓ
            </p>
          </div>
        ) : (
          <>
            {/* Bar Chart */}
            <div className="w-full h-72">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={topProducts} margin={{ top: 0, right: 0, left: -20, bottom: 0 }} barCategoryGap="30%">
                  <CartesianGrid vertical={false} stroke="rgba(255,255,255,0.04)" />
                  <XAxis
                    dataKey="name"
                    tick={{ fill: '#6b7280', fontSize: 11, fontWeight: 700 }}
                    axisLine={false} tickLine={false}
                    interval={0}
                    tickFormatter={(v) => v.length > 10 ? v.slice(0, 10) + '…' : v}
                  />
                  <YAxis
                    tick={{ fill: '#6b7280', fontSize: 11, fontWeight: 700 }}
                    axisLine={false} tickLine={false}
                    allowDecimals={false}
                  />
                  <Tooltip content={<CustomTooltip />} cursor={{ fill: 'rgba(255,255,255,0.03)' }} />
                  <Bar dataKey="sold" radius={[10, 10, 0, 0]} maxBarSize={52}>
                    {topProducts.map((_, idx) => (
                      <Cell key={idx} fill={BAR_COLORS[idx % BAR_COLORS.length]} fillOpacity={0.85} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Ranked progress list */}
            <div className="mt-8 space-y-3">
              {topProducts.map((product, i) => {
                const max = topProducts[0]?.sold || 1;
                const pct = Math.round((product.sold / max) * 100);
                return (
                  <div key={i} className="flex items-center gap-4">
                    <span className="text-[10px] font-black text-gray-600 w-5 text-right shrink-0">{i + 1}</span>
                    <div className="flex-1">
                      <div className="flex justify-between items-center mb-1.5">
                        <span className="text-xs font-bold text-gray-300 truncate max-w-50">{product.name}</span>
                        <span className="text-xs font-black text-white ml-4 shrink-0">{product.sold} sold</span>
                      </div>
                      <div className="h-1.5 bg-white/5 rounded-full overflow-hidden">
                        <motion.div
                          initial={{ width: 0 }}
                          animate={{ width: `${pct}%` }}
                          transition={{ delay: 0.4 + i * 0.06, duration: 0.7, ease: 'easeOut' }}
                          className="h-full rounded-full"
                          style={{ background: BAR_COLORS[i % BAR_COLORS.length] }}
                        />
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </>
        )}
      </motion.div>

      {/* PAID TRANSACTIONS TABLE */}
      <div className="bg-white/5 border border-white/10 rounded-[48px] p-10 overflow-hidden shadow-2xl backdrop-blur-lg">
        <div className="flex items-center justify-between mb-10">
          <h3 className="text-2xl font-black tracking-tight flex items-center gap-3 text-white uppercase">
            <CheckCircle className="text-green-500" /> Successful Transactions
          </h3>
          <span className="text-xs font-bold text-gray-500 bg-white/5 px-4 py-2 rounded-full border border-white/10">
            Showing only paid orders
          </span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left">
            <thead>
              <tr className="text-gray-500 text-[10px] font-black uppercase tracking-[0.2em] border-b border-white/5">
                <th className="pb-6">ID</th>
                <th className="pb-6">Customer</th>
                <th className="pb-6">Amount</th>
                <th className="pb-6 text-right">Verification</th>
              </tr>
            </thead>
            <tbody className="text-sm text-gray-300">
              {paidOrders.map((order: any) => (
                <tr key={order.id} className="border-b border-white/5 hover:bg-white/2 transition-colors">
                  <td className="py-6 font-bold text-gray-500">#{order.id}</td>
                  <td className="py-6">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 bg-indigo-600/20 rounded-full flex items-center justify-center text-[10px] font-bold text-indigo-400">
                        {(order.user__username ? order.user__username[0] : "U").toUpperCase()}
                      </div>
                      <span className="font-bold text-white">{order.user__username || "Guest User"}</span>
                    </div>
                  </td>
                  <td className="py-6 font-black text-white">${parseFloat(order.total_amount).toFixed(2)}</td>
                  <td className="py-6 text-right">
                    <span className="px-4 py-1.5 rounded-full text-[10px] font-black uppercase tracking-widest bg-green-500/10 text-green-400 border border-green-500/20 flex items-center gap-2 justify-end w-fit ml-auto">
                      <CheckCircle className="w-3 h-3" /> Verified Paid
                    </span>
                  </td>
                </tr>
              ))}
              {paidOrders.length === 0 && (
                <tr>
                  <td colSpan={4} className="py-20 text-center text-gray-600 font-bold text-sm uppercase tracking-widest">
                    No successful transactions found
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}