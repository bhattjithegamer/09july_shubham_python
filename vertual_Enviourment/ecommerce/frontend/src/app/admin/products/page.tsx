"use client";
import React, { useEffect, useState, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Plus, Pencil, Trash2, X, Check, Loader2, Package, ImagePlus, Box } from 'lucide-react';

const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

const CATEGORIES = [
  'Elite Laptops',
  'Mechanical Keyboards',
  'Pro Peripherals',
  'Workstation Setup',
];

interface Product {
  id: number;
  name: string;
  category: string;
  price: string;
  description: string;
  stock: number;
  image?: string;
}

const empty = { name: '', category: CATEGORIES[0], price: '', description: '', stock: '0' };

export default function AdminProducts() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [form, setForm] = useState(empty);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [editId, setEditId] = useState<number | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [toast, setToast] = useState('');
  const [priceError, setPriceError] = useState('');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const token = () => typeof window !== "undefined" ? localStorage.getItem('token') : null;
  const showToast = (msg: string) => { setToast(msg); setTimeout(() => setToast(''), 2500); };

  const getImageUrl = (path?: string) => {
    if (!path) return null;
    if (path.startsWith('http')) return path;
    return `${API}${path}`;
  };

  const fetchProducts = async () => {
    try {
      const res = await fetch(`${API}/api/stats/products/`, {
        headers: { Authorization: `Bearer ${token()}` }
      });
      if (!res.ok) throw new Error("Failed to fetch");
      const data = await res.json();
      setProducts(data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchProducts(); }, []);

  const openAdd = () => {
    setForm(empty);
    setSelectedFile(null);
    setImagePreview(null);
    setEditId(null);
    setPriceError('');
    setShowForm(true);
  };

  const openEdit = (p: Product) => {
    setForm({ 
      name: p.name, 
      category: p.category || CATEGORIES[0], 
      price: p.price, 
      description: p.description,
      stock: p.stock?.toString() || '0' 
    });
    setSelectedFile(null);
    setImagePreview(getImageUrl(p.image));
    setEditId(p.id);
    setPriceError('');
    setShowForm(true);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setSelectedFile(file);
    setImagePreview(URL.createObjectURL(file));
  };

  // ── Price validation on change ──
  const handlePriceChange = (val: string) => {
    setForm({ ...form, price: val });
    const num = parseFloat(val);
    if (val === '') {
      setPriceError('Price is required.');
    } else if (isNaN(num) || num <= 0) {
      setPriceError('Price must be greater than 0.');
    } else {
      setPriceError('');
    }
  };

  const handleSave = async () => {
    if (!form.name) { showToast('Artifact name is required.'); return; }

    const priceNum = parseFloat(form.price);
    if (!form.price || isNaN(priceNum) || priceNum <= 0) {
      setPriceError('Price must be greater than 0.');
      showToast('Invalid price — must be greater than 0.');
      return;
    }

    setSaving(true);

    const formData = new FormData();
    formData.append('name', form.name);
    formData.append('category', form.category);
    formData.append('price', form.price);
    formData.append('description', form.description);
    formData.append('stock', form.stock);

    if (selectedFile) formData.append('image', selectedFile);

    const url = editId
      ? `${API}/api/stats/products/edit/${editId}/`
      : `${API}/api/stats/products/add/`;

    try {
      const res = await fetch(url, {
        method: editId ? 'PATCH' : 'POST',
        headers: { Authorization: `Bearer ${token()}` },
        body: formData,
      });
      if (res.ok) {
        await fetchProducts();
        setShowForm(false);
        showToast(editId ? 'Stock & Product updated!' : 'Artifact added!');
      } else {
        showToast('Error saving product');
      }
    } catch {
      showToast('Network error');
    } finally {
      setSaving(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (!confirm('Delete this product?')) return;
    try {
      const res = await fetch(`${API}/api/stats/product-delete/${id}/`, {
        method: 'DELETE',
        headers: { Authorization: `Bearer ${token()}` },
      });
      if (res.ok) {
        setProducts(prev => prev.filter(p => p.id !== id));
        showToast('Product deleted successfully.');
      } else {
        showToast('Could not delete from server.');
      }
    } catch (err) {
      showToast('Network error.');
      console.error(err);
    }
  };

  return (
    <div className="relative z-10 space-y-10 p-4 min-h-screen text-white">
      {/* Toast */}
      <AnimatePresence>
        {toast && (
          <motion.div initial={{ y: -20, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={{ opacity: 0 }}
            className="fixed top-6 right-6 z-50 bg-indigo-600 text-white px-6 py-3 rounded-2xl font-bold shadow-2xl text-sm">
            {toast}
          </motion.div>
        )}
      </AnimatePresence>

      {/* Header */}
      <header className="flex items-center justify-between px-2">
        <div>
          <h2 className="text-4xl font-black tracking-tight">Bhattji Inventory</h2>
          <p className="text-gray-500 text-xs uppercase tracking-widest mt-1">Monitor Artifact Levels</p>
        </div>
        <motion.button whileTap={{ scale: 0.95 }} onClick={openAdd}
          className="bg-indigo-600 text-white px-5 py-3 rounded-2xl font-bold flex items-center gap-2 text-sm shadow-xl hover:bg-indigo-700 transition">
          <Plus className="w-4 h-4" /> Add Artifact
        </motion.button>
      </header>

      {/* Form Overlay */}
      <AnimatePresence>
        {showForm && (
          <motion.div initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -20 }}
            className="bg-white/5 border border-white/10 rounded-[40px] p-8 space-y-6 backdrop-blur-xl">
            <h3 className="font-black text-2xl text-indigo-400 italic">{editId ? 'Update Artifact' : 'New Artifact'}</h3>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <input placeholder="Artifact Name" value={form.name}
                onChange={e => setForm({ ...form, name: e.target.value })}
                className="bg-white/5 border border-white/10 rounded-2xl px-5 py-4 text-sm text-white outline-none focus:ring-2 focus:ring-indigo-500" />

              {/* Price field with validation */}
              <div className="flex flex-col gap-1">
                <input
                  placeholder="Value (Price)"
                  type="number"
                  min="0.01"
                  step="0.01"
                  value={form.price}
                  onChange={e => handlePriceChange(e.target.value)}
                  className={`bg-white/5 border rounded-2xl px-5 py-4 text-sm text-white outline-none focus:ring-2 transition
                    ${priceError
                      ? 'border-red-500/60 focus:ring-red-500 bg-red-500/5'
                      : 'border-white/10 focus:ring-indigo-500'
                    }`}
                />
                {priceError && (
                  <p className="text-[10px] text-red-400 font-bold px-1">{priceError}</p>
                )}
              </div>

              <div className="relative">
                <Box className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-500" />
                <input placeholder="Stock Qty" type="number" value={form.stock}
                  onChange={e => setForm({ ...form, stock: e.target.value })}
                  className="w-full bg-white/5 border border-white/10 rounded-2xl px-5 pl-12 py-4 text-sm text-white outline-none focus:ring-2 focus:ring-indigo-500" />
              </div>

              <select value={form.category} onChange={e => setForm({ ...form, category: e.target.value })}
                className="bg-[#0f0f1b] border border-white/10 rounded-2xl px-5 py-4 text-sm text-white outline-none focus:ring-2 focus:ring-indigo-500 cursor-pointer">
                {CATEGORIES.map(cat => (
                  <option key={cat} value={cat}>{cat}</option>
                ))}
              </select>
            </div>

            <textarea placeholder="Artifact description..." value={form.description} rows={3}
              onChange={e => setForm({ ...form, description: e.target.value })}
              className="w-full bg-white/5 border border-white/10 rounded-2xl px-5 py-4 text-sm text-white outline-none focus:ring-2 focus:ring-indigo-500 resize-none" />

            {/* Image Section */}
            <div className="flex flex-col sm:flex-row items-center gap-6 p-6 bg-white/5 rounded-[30px] border border-white/5">
              <div onClick={() => fileInputRef.current?.click()}
                className="w-32 h-32 rounded-3xl border-2 border-dashed border-white/20 flex items-center justify-center overflow-hidden cursor-pointer hover:border-indigo-500 transition-all bg-black/40">
                {imagePreview
                  ? <img src={imagePreview} alt="preview" className="w-full h-full object-cover" />
                  : <ImagePlus className="w-8 h-8 text-gray-600" />}
              </div>
              <div className="flex flex-col gap-3">
                <p className="text-xs font-black text-gray-500 uppercase tracking-[0.2em]">Visual Representation</p>
                <button onClick={() => fileInputRef.current?.click()}
                  className="bg-indigo-600 text-white px-6 py-2 rounded-xl text-xs font-bold hover:bg-indigo-700 transition">
                  Upload Artifact Image
                </button>
                <p className="text-[10px] text-gray-600">JPG, PNG or WEBP up to 5MB</p>
              </div>
              <input ref={fileInputRef} type="file" accept="image/*" className="hidden" onChange={handleFileChange} />
            </div>

            <div className="flex gap-4 pt-2">
              <motion.button whileTap={{ scale: 0.95 }} onClick={handleSave} disabled={saving || !!priceError}
                className="bg-green-600 text-white px-8 py-3 rounded-2xl font-bold text-sm flex items-center gap-2 hover:bg-green-700 disabled:opacity-50 transition">
                {saving ? <Loader2 className="w-4 h-4 animate-spin" /> : <Check className="w-4 h-4" />}
                {editId ? 'Apply Update' : 'Seal Artifact'}
              </motion.button>
              <button onClick={() => setShowForm(false)}
                className="bg-white/5 border border-white/10 px-8 py-3 rounded-2xl font-bold text-sm text-gray-400 hover:text-white transition">
                Cancel
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Main Inventory Table */}
      {loading ? (
        <div className="grid grid-cols-1 gap-4">
          {[1, 2, 3].map(i => <div key={i} className="h-20 bg-white/5 rounded-[30px] animate-pulse" />)}
        </div>
      ) : (
        <div className="bg-white/5 border border-white/10 rounded-[40px] overflow-hidden shadow-2xl">
          <table className="w-full text-left">
            <thead className="bg-white/5 border-b border-white/10">
              <tr className="text-gray-500 text-[10px] uppercase font-black tracking-widest">
                <th className="p-8">Artifact Details</th>
                <th className="p-8 hidden sm:table-cell">Stock Level</th>
                <th className="p-8">Market Value</th>
                <th className="p-8 text-right">Registry</th>
              </tr>
            </thead>
            <tbody>
              {products.map((p, i) => (
                <motion.tr key={p.id} initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: i * 0.05 }}
                  className="border-b border-white/5 hover:bg-white/3 transition-colors">
                  <td className="p-8">
                    <div className="flex items-center gap-4">
                      <div className="w-14 h-14 bg-black rounded-2xl overflow-hidden border border-white/10 shrink-0 shadow-lg">
                        {p.image
                          ? <img src={getImageUrl(p.image) || ""} alt={p.name} className="w-full h-full object-cover" />
                          : <Package className="w-6 h-6 m-4 text-indigo-500 opacity-50" />}
                      </div>
                      <div>
                        <p className="font-black text-sm text-white">{p.name}</p>
                        <p className="text-[10px] text-indigo-500 font-bold uppercase tracking-tighter mt-0.5">{p.category}</p>
                      </div>
                    </div>
                  </td>

                  <td className="p-8 hidden sm:table-cell">
                    <div className="flex flex-col gap-1.5">
                      <span className={`text-[10px] font-black uppercase tracking-widest ${p.stock <= 5 ? 'text-red-500' : 'text-green-500'}`}>
                        {p.stock === 0 ? 'Depleted' : p.stock <= 5 ? 'Critical' : 'Stocked'}
                      </span>
                      <div className="flex items-center gap-3">
                        <div className="w-20 h-1.5 bg-white/10 rounded-full overflow-hidden">
                          <div className={`h-full transition-all duration-1000 ${p.stock <= 5 ? 'bg-red-500' : 'bg-green-500'}`}
                            style={{ width: `${Math.min((p.stock / 20) * 100, 100)}%` }} />
                        </div>
                        <span className="text-xs font-mono font-bold text-gray-400">{p.stock}</span>
                      </div>
                    </div>
                  </td>

                  <td className="p-8 font-black text-indigo-400 text-lg">₹{p.price}</td>

                  <td className="p-8 text-right space-x-2">
                    <button onClick={() => openEdit(p)} className="p-3 bg-white/5 rounded-2xl text-gray-400 hover:text-indigo-400 hover:bg-indigo-400/10 transition-all">
                      <Pencil className="w-4 h-4" />
                    </button>
                    <button onClick={() => handleDelete(p.id)} className="p-3 bg-white/5 rounded-2xl text-gray-400 hover:text-red-500 hover:bg-red-500/10 transition-all">
                      <Trash2 className="w-4 h-4" />
                    </button>
                  </td>
                </motion.tr>
              ))}
            </tbody>
          </table>

          {products.length === 0 && (
            <div className="text-center py-24">
              <Package className="w-16 h-16 mx-auto mb-4 text-gray-800" />
              <p className="font-black text-gray-600 uppercase tracking-widest">Archive is empty</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}