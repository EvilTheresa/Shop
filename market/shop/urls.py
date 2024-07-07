from django.urls import path

from shop.views import index, create_product, detail_product, update_product, delete_product, create_category

urlpatterns = [
    path('', index, name='products'),
    path('create/', create_product, name='create_product'),
    path('categories/add/', create_category, name='create_category'),
    path('product/<int:pk>/', detail_product, name='detail_product'),
    path('product/<int:pk>/update/', update_product, name='update_product'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),
    ]