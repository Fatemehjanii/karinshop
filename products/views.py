from django.views import View
from django.shortcuts import render
from . import models


class ProductsDetails(View):
    def get(self, request):
        data_product_details = models.Product.objects.all()
        return render(request, 'products/product-details.html', {'data_product_details': data_product_details})


