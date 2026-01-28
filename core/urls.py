from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name='index'),
    path('error',views.error,name='error'),
    path('about',views.about,name='about'),
    path('alert',views.alert,name='alert'),
    path('article_details',views.article_details,name='article_details'),
    path('articles',views.articles,name='articles'),
    path('checkout',views.checkout,name='checkout'),

    path('contact',views.contact,name='contact'),

    path('empty_cart',views.empty_cart,name='empty_cart'),
    path('failed_payment',views.failed_payment,name='failed_payment'),
    path('payment',views.payment,name='payment'),
    # path('product_details',views.product_details,name='product_details'),
    path('questions',views.questions,name='questions'),
    path('shop/',views.shop,name='shop'),
    path('shopping_cart/',views.shopping_cart,name='shopping_cart'),
    path('successful_payment/',views.successful_payment,name='successful_payment'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)