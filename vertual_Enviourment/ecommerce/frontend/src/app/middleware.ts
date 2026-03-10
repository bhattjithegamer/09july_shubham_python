import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

const USER_PROTECTED = ['/profile', '/cart']
const ADMIN_PROTECTED = ['/admin']

export function middleware(request: NextRequest) {
  const token = request.cookies.get('token')?.value
  const isAdmin = request.cookies.get('is_admin')?.value === 'true'
  const { pathname } = request.nextUrl

  // Login નથી → /profile, /cart block
  const isUserRoute = USER_PROTECTED.some(r => pathname.startsWith(r))
  if (isUserRoute && !token) {
    const url = new URL('/login', request.url)
    url.searchParams.set('next', pathname)
    return NextResponse.redirect(url)
  }

  // Admin નથી → /admin block
  const isAdminRoute = ADMIN_PROTECTED.some(r => pathname.startsWith(r))
  if (isAdminRoute && !isAdmin) {
    return NextResponse.redirect(new URL('/', request.url))
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/profile/:path*', '/cart/:path*', '/admin/:path*'],
}