from django.urls import path
from .import views

urlpatterns = [
    path('pencatatan/', views.BarangList.as_view()),
]
