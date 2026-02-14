from django.urls import path, include
from . import views

urlpatterns = [
    path('api/',views.ListArticlesView.as_view(), name='article_list')
]
