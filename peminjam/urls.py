from django.urls import path
from .import views

urlpatterns = [
    path('barang/', views.Barang_list),
    path('barang/<int:pk>/', views.Peminjaman_detail),
]