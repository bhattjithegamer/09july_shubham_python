"use client";
import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  ShoppingCart, 
  CheckCircle, 
  Clock, 
  RefreshCw, 
  Package, 
  Truck, 
  XCircle, 
  AlertCircle,
  Search,
  CalendarDays,
  Download
} from 'lucide-react';

const API = process.env.NEXT_PUBLIC_API_URL || "http://https://ecommerce-backend-pgyl.onrender.com";

const STATUS_OPTIONS = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"];

const STATUS_CONFIG: Record<string, { color: string; bg: string; border: string; icon: React.ReactNode }> = {
  Pending:    { color: 'text-yellow-400',  bg: 'bg-yellow-500/10',  border: 'border-yellow-500/20', icon: <Clock className="w-3 h-3" /> },
  Processing: { color: 'text-blue-400',    bg: 'bg-blue-500/10',    border: 'border-blue-500/20',   icon: <Package className="w-3 h-3" /> },
  Shipped:    { color: 'text-indigo-400',  bg: 'bg-indigo-500/10',  border: 'border-indigo-500/20', icon: <Truck className="w-3 h-3" /> },
  Delivered:  { color: 'text-green-400',   bg: 'bg-green-500/10',   border: 'border-green-500/20',  icon: <CheckCircle className="w-3 h-3" /> },
  Cancelled:  { color: 'text-red-400',     bg: 'bg-red-500/10',     border: 'border-red-500/20',    icon: <XCircle className="w-3 h-3" /> },
};

interface Order {
  id: number;
  order_id: string;
  user__username: string;
  total_amount: string;
  is_paid: boolean;
  status: string;
  created_at: string;
}

// ── Invoice Download ──
const downloadInvoice = (order: Order) => {
  const date = order.created_at
    ? new Date(order.created_at).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
    : '—';
  const time = order.created_at
    ? new Date(order.created_at).toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' })
    : '';
  const status = order.status || 'Pending';
  const paid = order.is_paid ? 'PAID' : 'PENDING';

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <title>Invoice #${order.id}</title>
  <style>
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: 'Segoe UI', sans-serif; background:#fff; color:#111; padding:48px; }
    .header { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:40px; }
    .brand { font-size:28px; font-weight:900; letter-spacing:-1px; color:#4f46e5; }
    .brand span { color:#111; }
    .invoice-label { text-align:right; }
    .invoice-label h2 { font-size:22px; font-weight:900; color:#111; }
    .invoice-label p { font-size:12px; color:#6b7280; margin-top:4px; }
    .divider { border:none; border-top:1.5px solid #e5e7eb; margin:24px 0; }
    .meta { display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-bottom:32px; }
    .meta-box label { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:.12em; color:#9ca3af; }
    .meta-box p { font-size:15px; font-weight:700; margin-top:4px; color:#111; }
    .table { width:100%; border-collapse:collapse; margin-bottom:32px; }
    .table th { text-align:left; font-size:10px; font-weight:800; text-transform:uppercase; letter-spacing:.15em; color:#9ca3af; padding:10px 12px; border-bottom:1.5px solid #e5e7eb; }
    .table td { padding:14px 12px; font-size:14px; border-bottom:1px solid #f3f4f6; color:#374151; }
    .total-row td { font-weight:900; font-size:16px; color:#111; border-bottom:none; border-top:2px solid #111; padding-top:16px; }
    .badge { display:inline-block; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:.1em; }
    .badge.paid { background:#dcfce7; color:#16a34a; }
    .badge.pending { background:#fef9c3; color:#ca8a04; }
    .footer { margin-top:48px; text-align:center; font-size:11px; color:#9ca3af; }
  </style>
</head>
<body>
  <div class="header">
    <div class="brand">NEXUS<span>.</span></div>
    <div class="invoice-label">
      <h2>INVOICE</h2>
      <p>#INV-${String(order.id).padStart(6, '0')}</p>
    </div>
  </div>
  <hr class="divider"/>
  <div class="meta">
    <div class="meta-box">
      <label>Customer</label>
      <p>${order.user__username || '—'}</p>
    </div>
    <div class="meta-box">
      <label>Order Date</label>
      <p>${date} &nbsp; ${time}</p>
    </div>
    <div class="meta-box">
      <label>Order ID</label>
      <p>#${order.id}</p>
    </div>
    <div class="meta-box">
      <label>Fulfillment Status</label>
      <p>${status}</p>
    </div>
  </div>
  <hr class="divider"/>
  <table class="table">
    <thead>
      <tr>
        <th>Description</th>
        <th style="text-align:right">Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Order #${order.id} — ${status}</td>
        <td style="text-align:right">$${parseFloat(order.total_amount).toFixed(2)}</td>
      </tr>
      <tr class="total-row">
        <td>Total &nbsp; <span class="badge ${order.is_paid ? 'paid' : 'pending'}">${paid}</span></td>
        <td style="text-align:right">$${parseFloat(order.total_amount).toFixed(2)}</td>
      </tr>
    </tbody>
  </table>
  <hr class="divider"/>
  <div class="footer">Thank you for shopping with BhattJi &nbsp;·&nbsp; Generated on ${new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'long', year: 'numeric' })}</div>
</body>
</html>`;

  const blob = new Blob([html], { type: 'text/html' });
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement('a');
  a.href     = url;
  a.download = `Invoice-${order.id}.html`;
  a.click();
  URL.revokeObjectURL(url);
};

export default function AdminOrders() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);
  const [updatingId, setUpdatingId] = useState<number | null>(null);
  const [toast, setToast] = useState('');

  // --- Search & Filter State ---
  const [search, setSearch] = useState('');
  const [dateFrom, setDateFrom] = useState('');
  const [dateTo, setDateTo] = useState('');

  const token = () => typeof window !== "undefined" ? localStorage.getItem('token') : null;

  const showToast = (msg: string) => { 
    setToast(msg); 
    setTimeout(() => setToast(''), 3000); 
  };

  const fetchOrders = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API}/api/stats/orders/`, {
        headers: { Authorization: `Bearer ${token()}` }
      });
      if (!res.ok) throw new Error("Failed to fetch");
      const data = await res.json();
      setOrders(data);
    } catch (error) {
      showToast("Error loading orders");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchOrders(); }, []);

  const handleUpdate = async (id: number, payload: any) => {
    setUpdatingId(id);
    try {
      const res = await fetch(`${API}/api/stats/orders/update/${id}/`, {
        method: 'PATCH',
        headers: { 
          'Content-Type': 'application/json', 
          Authorization: `Bearer ${token()}` 
        },
        body: JSON.stringify(payload),
      });

      if (res.ok) {
        setOrders(prev => prev.map(order => 
          order.id === id ? { ...order, ...payload } : order
        ));
        showToast("Order updated successfully!");
      } else {
        showToast("Update failed!");
      }
    } catch (error) {
      showToast("Network error!");
    } finally {
      setUpdatingId(null);
    }
  };

  // --- Filtered Orders ---
  const filteredOrders = orders.filter(order => {
    const q = search.toLowerCase().trim();
    const matchesSearch = !q || (order.user__username || '').toLowerCase().includes(q);
    const orderDateStr = order.created_at ? order.created_at.slice(0, 10) : '';
    const matchesFrom = !dateFrom || orderDateStr >= dateFrom;
    const matchesTo   = !dateTo   || orderDateStr <= dateTo;
    return matchesSearch && matchesFrom && matchesTo;
  });

  const totalPaid = orders.filter(o => o.is_paid).length;

  const statusCounts = STATUS_OPTIONS.reduce((acc, s) => {
    acc[s] = orders.filter(o => (o.status || "Pending") === s).length;
    return acc;
  }, {} as Record<string, number>);

  return (
    <div className="relative z-10 space-y-10 p-4 min-h-screen text-white">
      {/* Toast Notification */}
      <AnimatePresence>
        {toast && (
          <motion.div 
            initial={{ y: -50, opacity: 0 }} 
            animate={{ y: 0, opacity: 1 }} 
            exit={{ y: -50, opacity: 0 }}
            className="fixed top-10 right-10 z-100 bg-indigo-600 px-6 py-3 rounded-2xl font-bold shadow-2xl flex items-center gap-2"
          >
            <AlertCircle className="w-4 h-4" /> {toast}
          </motion.div>
        )}
      </AnimatePresence>

      {/* Header */}
      <header className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-4xl font-black tracking-tight uppercase">Order Management</h2>
          <p className="text-gray-500 text-xs tracking-[0.2em] mt-1">Track payments and fulfillment status</p>
        </div>
        <button 
          onClick={fetchOrders} 
          disabled={loading}
          className="p-4 bg-white/5 border border-white/10 rounded-2xl text-gray-400 hover:text-white transition-all disabled:opacity-50"
        >
          <RefreshCw className={`w-5 h-5 ${loading ? 'animate-spin' : ''}`} />
        </button>
      </header>

      {/* Row 1: Payment Stats */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        {[
          { label: 'Total Orders', value: orders.length, color: 'text-white' },
          { label: 'Paid Orders', value: totalPaid, color: 'text-green-400' },
        ].map((stat, i) => (
          <div key={i} className="bg-white/5 border border-white/10 rounded-3xl p-6 text-center backdrop-blur-md">
            <h3 className={`text-3xl font-black ${stat.color}`}>{stat.value}</h3>
            <p className="text-gray-500 text-[10px] uppercase font-bold tracking-widest mt-2">{stat.label}</p>
          </div>
        ))}
      </div>

      {/* Row 2: Status-wise counts */}
      <div className="grid grid-cols-2 sm:grid-cols-5 gap-4">
        {STATUS_OPTIONS.map((status) => {
          const cfg = STATUS_CONFIG[status];
          return (
            <div key={status} className={`${cfg.bg} border ${cfg.border} rounded-[20px] p-4 text-center backdrop-blur-md`}>
              <div className={`flex items-center justify-center gap-1.5 mb-2 ${cfg.color}`}>
                {cfg.icon}
                <span className="text-[10px] font-black uppercase tracking-widest">{status}</span>
              </div>
              <h3 className={`text-2xl font-black ${cfg.color}`}>{statusCounts[status]}</h3>
            </div>
          );
        })}
      </div>

      {/* Search & Date Filter */}
      <div className="flex flex-col sm:flex-row gap-3">
        <div className="relative flex-1">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500 pointer-events-none" />
          <input
            type="text"
            placeholder="Search by Customer Name..."
            value={search}
            onChange={e => setSearch(e.target.value)}
            className="w-full bg-white/5 border border-white/10 rounded-2xl pl-11 pr-4 py-3 text-sm text-white placeholder-gray-600 outline-none focus:ring-2 focus:ring-indigo-500 transition"
          />
        </div>
        <div className="relative">
          <CalendarDays className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500 pointer-events-none" />
          <input
            type="date"
            value={dateFrom}
            onChange={e => setDateFrom(e.target.value)}
            className="bg-white/5 border border-white/10 rounded-2xl pl-11 pr-4 py-3 text-sm text-white outline-none focus:ring-2 focus:ring-indigo-500 transition scheme-dark"
          />
        </div>
        <div className="relative">
          <CalendarDays className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500 pointer-events-none" />
          <input
            type="date"
            value={dateTo}
            onChange={e => setDateTo(e.target.value)}
            className="bg-white/5 border border-white/10 rounded-2xl pl-11 pr-4 py-3 text-sm text-white outline-none focus:ring-2 focus:ring-indigo-500 transition scheme-dark"
          />
        </div>
        {(search || dateFrom || dateTo) && (
          <button
            onClick={() => { setSearch(''); setDateFrom(''); setDateTo(''); }}
            className="px-4 py-3 bg-red-500/10 border border-red-500/20 text-red-400 text-xs font-black rounded-2xl hover:bg-red-500/20 transition whitespace-nowrap"
          >
            Clear
          </button>
        )}
      </div>

      {(search || dateFrom || dateTo) && (
        <p className="text-xs text-gray-500 font-bold -mt-6">
          Showing {filteredOrders.length} of {orders.length} orders
        </p>
      )}

      {/* Table Section */}
      <div className="bg-white/5 border border-white/10 rounded-4xl overflow-hidden backdrop-blur-xl shadow-2xl">
        <div className="overflow-x-auto">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b border-white/10 text-gray-500 text-[10px] uppercase font-black tracking-widest">
                <th className="p-6">Order ID</th>
                <th className="p-6">Customer</th>
                <th className="p-6">Date</th>
                <th className="p-6">Total Amount</th>
                <th className="p-6">Payment</th>
                <th className="p-6">Order Status</th>
                <th className="p-6">Invoice</th>
              </tr>
            </thead>
            <tbody>
              {loading ? (
                [1, 2, 3].map(i => (
                  <tr key={i} className="animate-pulse">
                    <td colSpan={7} className="p-6"><div className="h-8 bg-white/5 rounded-xl w-full" /></td>
                  </tr>
                ))
              ) : filteredOrders.length > 0 ? (
                filteredOrders.map((order) => {
                  const currentStatus = order.status || "Pending";
                  const cfg = STATUS_CONFIG[currentStatus] ?? STATUS_CONFIG["Pending"];

                  return (
                    <tr key={order.id} className="border-b border-white/5 hover:bg-white/2 transition-colors">
                      <td className="p-6 font-mono text-indigo-400 text-sm">#{order.id}</td>

                      <td className="p-6">
                        <div className="flex items-center gap-3">
                          <div className="w-8 h-8 bg-indigo-500/20 rounded-full flex items-center justify-center text-xs font-bold text-indigo-400">
                            {order.user__username?.charAt(0).toUpperCase()}
                          </div>
                          <span className="font-bold text-sm">{order.user__username}</span>
                        </div>
                      </td>

                      <td className="p-6">
                        <div className="text-sm text-gray-400 font-bold">
                          {order.created_at
                            ? new Date(order.created_at).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
                            : '—'}
                        </div>
                        <div className="text-[10px] text-gray-600 mt-0.5">
                          {order.created_at
                            ? new Date(order.created_at).toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' })
                            : ''}
                        </div>
                      </td>

                      <td className="p-6 font-black text-white">
                        ${parseFloat(order.total_amount).toFixed(2)}
                      </td>

                      <td className="p-6">
                        <button 
                          onClick={() => handleUpdate(order.id, { is_paid: !order.is_paid })}
                          disabled={updatingId === order.id}
                          className={`px-4 py-2 rounded-xl text-[10px] font-black uppercase tracking-widest border transition-all flex items-center gap-2
                            ${order.is_paid 
                              ? 'bg-green-500/10 text-green-400 border-green-500/20 hover:bg-red-500/10 hover:text-red-400 hover:border-red-500/20' 
                              : 'bg-red-500/10 text-red-400 border-red-500/20 hover:bg-green-500/10 hover:text-green-400 hover:border-green-500/20'
                            }`}
                        >
                          {updatingId === order.id ? (
                            <RefreshCw className="w-3 h-3 animate-spin" />
                          ) : order.is_paid ? (
                            <><CheckCircle className="w-3 h-3" /> Paid</>
                          ) : (
                            <><Clock className="w-3 h-3" /> Pending</>
                          )}
                        </button>
                      </td>

                      <td className="p-6">
                        <div className="flex items-center gap-3">
                          <span className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-[10px] font-black uppercase tracking-widest border transition-all
                            ${cfg.bg} ${cfg.color} ${cfg.border}`}
                          >
                            {updatingId === order.id
                              ? <RefreshCw className="w-3 h-3 animate-spin" />
                              : cfg.icon
                            }
                            {currentStatus}
                          </span>
                          <select 
                            value={currentStatus}
                            onChange={(e) => handleUpdate(order.id, { status: e.target.value })}
                            disabled={updatingId === order.id}
                            className="bg-black/40 border border-white/10 rounded-xl px-3 py-2 text-xs font-bold text-white outline-none focus:ring-2 focus:ring-indigo-500 cursor-pointer disabled:opacity-50"
                          >
                            {STATUS_OPTIONS.map(status => (
                              <option key={status} value={status} className="bg-gray-900">{status}</option>
                            ))}
                          </select>
                        </div>
                      </td>

                      {/* ── Invoice Download ── */}
                      <td className="p-6">
                        <button
                          onClick={() => downloadInvoice(order)}
                          title="Download Invoice"
                          className="flex items-center gap-2 px-3 py-2 bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-[10px] font-black rounded-xl hover:bg-indigo-500/20 transition-all uppercase tracking-widest"
                        >
                          <Download className="w-3 h-3" /> Invoice
                        </button>
                      </td>

                    </tr>
                  );
                })
              ) : (
                <tr>
                  <td colSpan={7} className="p-20 text-center text-gray-500">
                    <ShoppingCart className="w-12 h-12 mx-auto mb-4 opacity-20" />
                    <p className="font-bold uppercase tracking-widest">No orders found</p>
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