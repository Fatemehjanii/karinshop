from django.shortcuts import render
from products import models
from django.views import View



# def NewProducts(request):
#     new_data_products = models.Product.objects.all()[:10]
#     return render(request, 'core/index.html', {'data_products': data_products})

def base(request):
    data_products = models.Product.objects.all()
    return render(request, 'base.html', {'data_products': data_products})


def error(request):
    return render(request, 'core/404.html')

def about(request):
    return render(request,'core/aboute-us.html')

def alert(request):
    return render(request,'core/alert.html')

def article_details(request):
    return render(request,'core/article-details.html')

def articles(request):
    return render(request,'core/articles.html')

def checkout(request):
    return render(request,'core/checkout.html')


def contact(request):
    return render(request,'core/contact-us.html')


def empty_cart(request):
    return render(request,'core/empty-cart.html')

def failed_payment(request):
    return render(request,'core/failed-payment.html')

def payment(request):
    return render(request,'core/payment.html')



def questions(request):
    return render(request,'core/questions.html')

def shop(request):
    return render(request,'products/shop.html')

def shopping_cart(request):
    return render(request,'core/shopping-cart.html')

def successful_payment(request):
    return render(request,'core/successful-payment.html')






