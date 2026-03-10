# 🛡️ Nexus Tech: Professional Full-Stack E-Commerce Solution

Nexus Tech is a high-performance, specialized e-commerce platform designed for tech enthusiasts. Built with the latest **Next.js 15+** and **Django REST Framework**, it features a secure shopping experience, real-time inventory management, and a powerful administrative dashboard.

---

## 🛠 Tech Stack

| Component           | Technology                                                         |
| :------------------ | :----------------------------------------------------------------- |
| **Frontend**        | Next.js 15 (App Router), React 19, Tailwind CSS v4, Framer Motion |
| **Backend**         | Django 5.x, Django REST Framework (DRF)                            |
| **Database**        | PostgreSQL (Production Grade)                                      |
| **Authentication**  | SimpleJWT (Access/Refresh Tokens), Google OAuth 2.0                |
| **Payment Gateway** | Razorpay SDK (with Atomic Transaction Support)                     |
| **Icons & UI**      | Lucide React, Glassmorphism UI Design                              |

---

## ✨ Key Features

### 🛒 Customer Experience

- **Premium Catalog:** Specialized categories like Elite Laptops, Mechanical Keyboards, and Pro Peripherals.
- **Secure Authentication:** Dual support for Custom Email/Password and Google Social Login , You will still have to log in after registering.
- **Smart Shopping Cart:** Real-time stock validation and persistent cart experience.
- **Secure Payments:** Seamless Razorpay integration for safe and fast checkout.
- **Order Tracking:** Detailed order history with lifecycle status (Pending → Shipped → Delivered).

### 🛡️ Administrative Dashboard

- **Advanced Analytics:** Real-time metrics for Total Revenue, Total Orders, and Product Levels.
- **Inventory Management:** Full CRUD (Create, Read, Update, Delete) with image upload support.
- **Best Sellers:** Automated calculation of top-selling products using Django Aggregation.
- **Order Lifecycle Management:** Update payment status and shipping progress manually.
- **Stock Guard:** Atomic database operations to prevent overselling during high traffic.

---

## 📁 Project Structure

```text
├── backend/
│   ├── ecommerce/          # Main Settings & Root URLs
│   ├── myapp/              # Core Logic (Auth, Products, Orders)
│   ├── dashboard/          # Admin Panel APIs & Statistics
│   └── media/              # Product Images
│
└── frontend/
    └── src/
        ├── app/            # Next.js App Router Pages
        ├── components/     # Reusable UI Components
        └── utils/          # API Helper Functions
```

---

## 🔌 API Endpoints

| Method | Endpoint                  | Description                              |
| :----- | :------------------------ | :--------------------------------------- |
| POST   | `/api/login/`             | User Authentication & JWT Generation     |
| GET    | `/api/get_products/`      | Fetch all available products             |
| GET    | `/api/products/<id>/`     | Detailed view of a single product        |
| POST   | `/api/create-payment/`    | Initialize Razorpay payment order        |
| POST   | `/api/payment-success/`   | Verify payment & deduct stock (Atomic)   |
| GET    | `/api/stats/stats/`       | Dashboard Statistics (Admin Only)        |
| POST   | `/api/stats/admin-login/` | Admin Authentication                     |

---

## ⚙️ Installation & Setup

### 1. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
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

Create a `.env` file in the `backend/` directory:

```env
SECRET_KEY=your_django_secret_key
GOOGLE_CLIENT_ID=your_google_oauth_client_id
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_secret_key
DATABASE_URL=your_postgresql_connection_string
```

---

## 🔒 Security & Optimization

- **Atomic Transactions:** `transaction.atomic()` ensures stock is only reduced after successful payment.
- **Race Condition Prevention:** `select_for_update()` handles high-volume simultaneous orders safely.
- **JWT Security:** 1-day access token and 7-day refresh token cycle.
- **CORS Management:** Strict Cross-Origin rules to protect backend APIs.
- **Centralized Logging:** `debug.log` system for monitoring transaction failures and errors.

---

## 🔑 Demo Credentials (Admin Dashboard)

For testing purposes, you can use the following default credentials to access the Admin Panel:

| Role          | Username      | Password  |
| :------------ | :------------ | :-------- |
| **Administrator** | `shubham` | `bhatt` |

> **Note:** These credentials are for demo purposes as defined in the `dashboard/views.py`. In a production environment, please use `python manage.py createsuperuser` and update the login logic for better security.

## 👨‍💻 Author

Built with ❤️ by **Shubham Bhatt**