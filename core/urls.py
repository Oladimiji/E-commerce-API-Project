from django.urls import path
from .views import (
    RegisterView,
    ProductListCreateView,
    ProductDetailView,
    CartRetrieveView,
    CartItemCreateView,
    CartItemDetailView,
    CheckoutView,
)

urlpatterns = [
    # Auth URLs
    path('register/', RegisterView.as_view(), name='register'),
    
    # Product URLs
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    # Cart URLs
    path('cart/', CartRetrieveView.as_view(), name='cart-detail'),
    path('cart/items/', CartItemCreateView.as_view(), name='cart-item-list-create'),
    path('cart/items/<int:pk>/', CartItemDetailView.as_view(), name='cart-item-detail'),
    
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]