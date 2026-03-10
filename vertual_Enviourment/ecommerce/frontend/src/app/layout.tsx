// src/app/layout.tsx
"use client";
import { usePathname } from "next/navigation";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";
import "./globals.css";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const isAdmin = pathname?.startsWith("/admin");

  return (
    <html lang="en" suppressHydrationWarning>
      <body suppressHydrationWarning>
        {!isAdmin && <Header />}
        <main>{children}</main>
        {!isAdmin && <Footer />}
      </body>
    </html>
  );
}