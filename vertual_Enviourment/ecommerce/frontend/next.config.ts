import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* images સેટિંગ્સ - જેથી Render પરથી ફોટા દેખાય */
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'ecommerce-backend-pgyl.onrender.com',
      },
    ],
  },
  /* headers સેટિંગ્સ - જેથી Google Login નું પોપ-અપ બ્લોક ના થાય */
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'Cross-Origin-Opener-Policy',
            value: 'same-origin-allow-popups',
          },
        ],
      },
    ];
  },
};

export default nextConfig;