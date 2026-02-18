from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet
from . import views

# router = DefaultRouter()
# router.register(r'articles', ArticleViewSet, basename='article')
#
# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

from . import views
from django.urls import path,include


urlpatterns = [
    path('list/', views.ArticleViewSet.as_view({"get": "list"}), name='create_blog'),
    path('retrive/<str:pk>/', views.ArticleViewSet.as_view({"get": "retrieve"}), name='create_blog'),
]