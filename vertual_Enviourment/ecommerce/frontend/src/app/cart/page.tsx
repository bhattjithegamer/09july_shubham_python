"use client";

import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Trash2, ShoppingBag, ArrowLeft, Plus, Minus, CheckCircle, XCircle, Loader2 } from "lucide-react";

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

type PaymentStatus = "idle" | "processing" | "success" | "failed";

export default function CartPage() {
  const [cart, setCart] = useState<any[]>([]);
  const [total, setTotal] = useState(0);
  const [loading, setLoading] = useState(true);
  const [paymentStatus, setPaymentStatus] = useState<PaymentStatus>("idle");
  const [paymentError, setPaymentError] = useState("");

  const calculateTotal = (items: any[]) => {
    const sum = items.reduce((acc, item) => acc + parseFloat(item.price) * (item.quantity || 1), 0);
    setTotal(sum);
  };

  useEffect(() => {
    const username = localStorage.getItem("username") || "guest";
    const savedCart = JSON.parse(localStorage.getItem(`cart_${username}`) || "[]");
    const merged: any[] = [];
    savedCart.forEach((item: any) => {
      const found = merged.find((p) => p.id === item.id);
      if (found) { found.quantity = (found.quantity || 1) + 1; }
      else { merged.push({ ...item, quantity: item.quantity || 1 }); }
    });
    setCart(merged);
    calculateTotal(merged);
    setLoading(false);
  }, []);

  const saveCart = (newCart: any[]) => {
    const username = localStorage.getItem("username") || "guest";
    localStorage.setItem(`cart_${username}`, JSON.stringify(newCart));
    setCart(newCart);
    calculateTotal(newCart);
    window.dispatchEvent(new Event("cartUpdated"));
  };

  const removeItem = (index: number) => {
    const newCart = [...cart];
    newCart.splice(index, 1);
    saveCart(newCart);
  };

  const changeQuantity = (index: number, delta: number) => {
    const newCart = [...cart];
    newCart[index].quantity = (newCart[index].quantity || 1) + delta;
    if (newCart[index].quantity <= 0) newCart.splice(index, 1);
    saveCart(newCart);
  };

  // ── Image URL helper ──
  const getImageUrl = (image?: string) => {
    if (!image) return null;
    if (image.startsWith("http://") || image.startsWith("https://")) return image;
    return `${API}${image.startsWith("/") ? "" : "/"}${image}`;
  };

  const handlePayment = async () => {
    const token = localStorage.getItem("token");
    const username = localStorage.getItem("username") || "guest";

    if (!token) {
      alert("Please login!");
      window.location.href = "/login";
      return;
    }

    setPaymentStatus("processing");
    setPaymentError("");

    try {
      const items = cart.map(item => ({
        id: item.id,
        name: item.name,
        price: item.price,
        quantity: item.quantity || 1,
      }));

      const res = await fetch(`${API}/api/create-payment/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ amount: total, items }),
      });

      if (res.status === 401) {
        const errorMsg = await res.json();
        console.log("Auth Error Details:", errorMsg);
        localStorage.removeItem("token");
        alert("Session expired. Please login again.");
        window.location.href = "/login";
        return;
      }

      if (!res.ok) throw new Error("Failed to create payment order.");
      const data = await res.json();

      await new Promise((resolve) => setTimeout(resolve, 1500));

      const verifyRes = await fetch(`${API}/api/payment-success/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({
          razorpay_order_id: data.order_id,
          razorpay_payment_id: `pay_DUMMY_${Date.now()}`,
        }),
      });

      if (verifyRes.status === 401) {
        localStorage.removeItem("token");
        alert("Session expired. Please login again.");
        window.location.href = "/login";
        return;
      }

      if (!verifyRes.ok) throw new Error("Payment confirmation failed.");

      setPaymentStatus("success");
      localStorage.removeItem(`cart_${username}`);
      setCart([]);
      setTotal(0);
      window.dispatchEvent(new Event("cartUpdated"));

    } catch (err: any) {
      setPaymentStatus("failed");
      setPaymentError(err.message || "Payment failed. Please try again.");
    }
  };

  if (loading) return (
    <div className="min-h-screen bg-[#050505] flex items-center justify-center text-white">
      Loading Cart...
    </div>
  );

  if (paymentStatus === "success") return (
    <div className="min-h-screen bg-[#050505] flex items-center justify-center text-white p-6">
      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        className="text-center bg-white/5 border border-white/10 rounded-[48px] p-16 max-w-md w-full"
      >
        <CheckCircle className="w-20 h-20 text-green-400 mx-auto mb-6" />
        <h2 className="text-4xl font-black mb-3">Payment Successful!</h2>
        <p className="text-gray-500 mb-10">Your order has been placed. Thank you for shopping with Bhatt Ji Store.</p>
        <button onClick={() => window.location.href = "/profile"}
          className="w-full bg-indigo-600 py-4 rounded-2xl font-black hover:bg-indigo-700 transition">
          View My Orders
        </button>
      </motion.div>
    </div>
  );

  return (
    <div className="min-h-screen bg-[#050505] text-white p-6 sm:p-20 font-sans relative">
      <button onClick={() => window.location.href = '/'} className="flex items-center gap-2 text-gray-500 hover:text-white transition mb-10">
        <ArrowLeft className="w-5 h-5" /> Continue Shopping
      </button>

      <div className="max-w-5xl mx-auto">
        <h2 className="text-5xl font-black mb-12 flex items-center gap-4">
          <ShoppingBag className="text-indigo-500" /> Your Cart
        </h2>

        <AnimatePresence>
          {paymentStatus === "failed" && (
            <motion.div initial={{ opacity: 0, y: -10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}
              className="flex items-center gap-4 bg-red-500/10 border border-red-500/30 text-red-400 rounded-2xl px-6 py-4 mb-8">
              <XCircle className="w-5 h-5 shrink-0" />
              <p className="text-sm font-bold">{paymentError}</p>
              <button onClick={() => setPaymentStatus("idle")} className="ml-auto text-xs underline">Dismiss</button>
            </motion.div>
          )}
        </AnimatePresence>

        {cart.length > 0 ? (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
            <div className="lg:col-span-2 space-y-6">
              {cart.map((item, index) => (
                <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} key={index}
                  className="bg-white/5 border border-white/10 p-6 rounded-4xl flex items-center justify-between gap-4">
                  <div className="flex items-center gap-6 flex-1 min-w-0">

                    {/* ── Fixed image display ── */}
                    <div className="w-16 h-16 bg-gray-900 rounded-2xl overflow-hidden shrink-0 flex items-center justify-center">
                      {getImageUrl(item.image)
                        ? <img src={getImageUrl(item.image)!} alt={item.name} className="w-full h-full object-cover" />
                        : <span className="text-2xl">📦</span>}
                    </div>

                    <div className="flex-1 min-w-0">
                      <h3 className="text-xl font-bold truncate">{item.name}</h3>
                      <p className="text-indigo-400 font-black mt-1">
                        ₹{(parseFloat(item.price) * (item.quantity || 1)).toFixed(2)}
                        {item.quantity > 1 && <span className="text-gray-500 text-sm font-normal ml-2">(₹{item.price} each)</span>}
                      </p>
                    </div>
                  </div>
                  <div className="flex items-center gap-2 shrink-0">
                    <div className="flex items-center gap-1 bg-white/5 border border-white/10 rounded-xl px-2 py-1">
                      <button onClick={() => changeQuantity(index, -1)} className="text-gray-400 hover:text-white transition p-1">
                        <Minus className="w-3 h-3" />
                      </button>
                      <span className="text-sm font-bold w-5 text-center">{item.quantity || 1}</span>
                      <button onClick={() => changeQuantity(index, +1)} className="text-gray-400 hover:text-white transition p-1">
                        <Plus className="w-3 h-3" />
                      </button>
                    </div>
                    <button onClick={() => removeItem(index)} className="text-red-500 p-3 bg-red-500/10 rounded-xl hover:bg-red-500 hover:text-white transition">
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </div>
                </motion.div>
              ))}
            </div>

            <div className="bg-white/5 p-8 rounded-[40px] border border-white/10 h-fit">
              <h3 className="text-2xl font-black mb-6">Summary</h3>
              <div className="space-y-3 mb-4">
                {cart.map((item, i) => (
                  <div key={i} className="flex justify-between text-sm text-gray-400">
                    <span className="truncate max-w-35">{item.name} × {item.quantity || 1}</span>
                    <span>₹{(parseFloat(item.price) * (item.quantity || 1)).toFixed(2)}</span>
                  </div>
                ))}
              </div>
              <div className="flex justify-between text-2xl font-black border-t border-white/10 pt-4">
                <span>Total</span>
                <span className="text-indigo-500">₹{total.toFixed(2)}</span>
              </div>
              <button onClick={handlePayment} disabled={paymentStatus === "processing"}
                className="w-full bg-indigo-600 mt-8 py-4 rounded-2xl font-black hover:bg-indigo-700 transition flex items-center justify-center gap-2 disabled:opacity-60 disabled:cursor-not-allowed">
                {paymentStatus === "processing" ? <><Loader2 className="w-5 h-5 animate-spin" /> Processing...</> : "Pay Now"}
              </button>
            </div>
          </div>
        ) : (
          <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}
            className="text-center py-32 bg-white/5 rounded-[50px] border border-dashed border-white/10">
            <p className="text-gray-500 text-2xl mb-8">Your cart is empty.</p>
            <button onClick={() => window.location.href = '/'} className="bg-white text-black px-10 py-4 rounded-full font-bold">Start Shopping</button>
          </motion.div>
        )}
      </div>
    </div>
  );
}