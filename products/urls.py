from django.urls import path

from . import views

urlpatterns = [
    path('', views.products, name='productos'),
    path('<str:product_url>/', views.product),
]