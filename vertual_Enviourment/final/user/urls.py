from django.contrib import admin
from django.urls import path
from user import views  # core app na views import karo

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Main Pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('careers/', views.careers, name='careers'),

    # Shop & Product Pages
    path('shop/', views.shop, name='shop'),
    path('product/', views.product, name='product'),
    path('product-3d-viewer/', views.product_3d_viewer, name='product-3d-viewer'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist_page, name='wishlist_page'),
    path('toggle-wishlist/<int:pid>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('orders/', views.orders, name='orders'),
    path('order-success/', views.order_success, name='order-success'),
    path('search-results/', views.search_results, name='search-results'),

    # Auth Pages
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('user_logout/', views.user_logout, name='user_logout'),

    # Blog Pages
    path('blog/', views.blog, name='blog'),
    path('blog-item/', views.blog_item, name='blog-item'),

    # Legal Pages
    path('terms/', views.terms, name='terms'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),

    # Extra Pages (Dynamic pan banavi sakay, pan atyare static rakhiye)
    path('page-1/', views.page_1, name='page-1'),
    path('page-2/', views.page_2, name='page-2'),
    path('page-3/', views.page_3, name='page-3'),
    path('page-4/', views.page_4, name='page-4'),
    path('page-5/', views.page_5, name='page-5'),
    path('product/<int:id>/', views.product_details, name='product_details'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
]