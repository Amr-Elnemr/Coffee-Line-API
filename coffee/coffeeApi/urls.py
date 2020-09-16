from django.urls import path, re_path
from . import views

urlpatterns = [
    path('products/<str:type>/', views.ProductList.as_view()),
]