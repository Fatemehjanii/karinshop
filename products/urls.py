from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('ProductsDetails', views.ProductsDetails.as_view(), name='product_details'),
]