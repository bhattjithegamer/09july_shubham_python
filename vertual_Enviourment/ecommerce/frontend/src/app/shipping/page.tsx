"use client";
import React from 'react';
import { Truck } from 'lucide-react';

export default function ShippingPage() {
  return (
    <div className="min-h-screen bg-black text-white p-10 pt-32">
      <div className="max-w-4xl mx-auto space-y-10">
        <h1 className="text-5xl font-black uppercase flex items-center gap-4"><Truck className="text-indigo-500 w-12 h-12" /> Shipping Policy</h1>
        <div className="space-y-6 text-gray-400 leading-loose">
          <section>
            <h2 className="text-2xl font-bold text-white mb-2">Delivery Timeline</h2>
            <p>Orders are typically processed within 24-48 hours. Shipping takes 3-7 business days depending on your location.</p>
          </section>
          <section>
            <h2 className="text-2xl font-bold text-white mb-2">Shipping Charges</h2>
            <p>We offer free shipping on all orders above $100. For orders below $100, a flat fee of $10 applies.</p>
          </section>
          <section>
            <h2 className="text-2xl font-bold text-white mb-2">Tracking</h2>
            <p>Once your order is shipped, you will receive an email with a tracking number to monitor your delivery status.</p>
          </section>
        </div>
      </div>
    </div>
  );
}