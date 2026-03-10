import { RotateCcw } from 'lucide-react';

export default function ReturnsPage() {
  return (
    <div className="min-h-screen bg-black text-white p-10 pt-32">
      <div className="max-w-4xl mx-auto space-y-8 text-center">
        <RotateCcw className="w-16 h-16 text-indigo-500 mx-auto" />
        <h1 className="text-5xl font-black">RETURNS & REFUNDS</h1>
        <p className="text-gray-400 text-xl">At Bhatt Ji Store, we ensure you are happy with every purchase.</p>
        
        <div className="text-left mt-16 space-y-8">
          <div className="bg-white/5 p-8 rounded-4xl border border-white/10">
            <h2 className="text-2xl font-bold mb-4">7-Day Return Policy</h2>
            <p className="text-gray-400">If the product is damaged or not as described, you can initiate a return within 7 days of delivery.</p>
          </div>
          <div className="bg-white/5 p-8 rounded-4xl border border-white/10">
            <h2 className="text-2xl font-bold mb-4">Refund Process</h2>
            <p className="text-gray-400">Once we receive the item and verify its condition, the refund will be processed to your original payment method within 5-7 business days.</p>
          </div>
        </div>
      </div>
    </div>
  );
}