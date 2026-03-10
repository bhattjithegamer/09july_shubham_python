# 🛡️ Nexus Tech: Professional Full-Stack E-Commerce Solution

> Nexus Tech is a high-performance, specialized e-commerce platform designed for tech enthusiasts. Built with the latest **Next.js 15+** and **Django REST Framework**, it features a secure shopping experience, real-time inventory management, and persistent cloud storage for product media.

---

## 🚀 Live Demo

| Portal | URL |
|--------|-----|
| **Frontend (Production)** | [https://09july-shubham-python.vercel.app](https://09july-shubham-python.vercel.app) |
| **Backend API** | [https://ecommerce-backend-pgyl.onrender.com](https://ecommerce-backend-pgyl.onrender.com) |

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Next.js 15 (App Router), React 19, Tailwind CSS v4, Framer Motion |
| **Backend** | Django 5.x, Django REST Framework (DRF) |
| **Database** | PostgreSQL (Production Grade via Render) |
| **Cloud Storage** | Cloudinary (Persistent Product Images) |
| **Authentication** | SimpleJWT (Access/Refresh Tokens), Google OAuth 2.0 |
| **Payment Gateway** | Razorpay SDK (Test Mode) |
| **Deployment** | Vercel (Frontend), Render (Backend) |

---

## ✨ Key Features

### 🛒 Customer Experience

- **Premium Catalog** — Specialized categories like Elite Laptops and Mechanical Keyboards
- **Dual Authentication** — Secure login via traditional Email/Password or Google Social Login
- **Smart Cart** — Persistent shopping cart with real-time stock validation
- **Secure Checkout** — Integrated Razorpay payment gateway for seamless transactions

### 🛡️ Administrative Dashboard

- **Advanced Analytics** — Real-time metrics for Revenue, Orders, and Inventory
- **Persistent Media** — Cloudinary integration ensures images are never lost on server restarts
- **Inventory Management** — Full CRUD operations for product catalogs
- **Stock Guard** — Atomic database operations to prevent overselling

---

## 📁 Project Structure

```
├── vertual_Enviourment/
│   └── ecommerce/          # Django Backend Source
│       ├── ecommerce/      # Project Settings & URLs
│       ├── myapp/          # Core Logic (Auth, Products, Orders)
│       └── dashboard/      # Admin Panel APIs & Statistics
│
└── frontend/               # Next.js Frontend Source
    ├── src/app/            # App Router (Pages & Layouts)
    ├── components/         # Reusable UI Elements
    └── utils/              # API Client & Configurations
```

---

## 🔑 Demo Credentials (Admin Dashboard)

> To evaluate the Admin Panel, please use the following credentials:

| Portal | Username | Password |
|--------|----------|----------|
| **Nexus Admin Portal** | `shubham` | `bhatt` |
| **Alternative Admin** | `admin` | `admin123` |

---

## 💳 Test Payment Instructions

The store uses a **simulated payment flow** (Razorpay integration is mocked for demo purposes). No real card details are required.

**Step 1** — Add any product to the cart

**Step 2** — Proceed to **Checkout** and fill in dummy shipping details

**Step 3** — Click **Place Order / Pay Now**

**Step 4** — ✅ A **"Payment Successful"** message will be displayed immediately

> **Note:** Since this is a mock integration, no actual Razorpay popup or card fields will appear. The payment is auto-approved to simulate a successful transaction.

---

## ⚙️ Local Installation & Setup

### 1. Backend Setup

```bash
cd vertual_Enviourment/ecommerce
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 📝 Environment Variables

### Backend (`.env`)

```env
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
GOOGLE_CLIENT_ID=your_google_client_id
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### Frontend (`.env.local`)

```env
NEXT_PUBLIC_API_URL=your_backend_url
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your_google_client_id
```

---

## ⚠️ Known Limitations & Future Improvements

### Current Limitations

- **Render Free Tier** — Spins down after 15 minutes of inactivity. The first request may take ~45 seconds to wake the server.
- **Security** — Implemented `CorsMiddleware` and `CSRF_TRUSTED_ORIGINS` for secure cross-domain communication.

### 🗺️ Future Roadmap

- [ ] Implementation of Search with **ElasticSearch**
- [ ] Automated Email notifications via **SendGrid**
- [ ] Bulk CSV Product Upload for Admin

---

## 👨‍💻 Author

Built with ❤️ by **Shubham Bhatt**