from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.SignUpView.as_view(),name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_account/', views.dashboard_account, name='dashboard_account'),
    path('dashboard_address/', views.dashboard_address, name='dashboard_address'),
    path('dashboard_favorite/', views.dashboard_favorite, name='dashboard_favorite'),
    path('dashboard_messages/', views.dashboard_messages, name='dashboard_messages'),
    path('dashboard_orders/', views.dashboard_orders, name='dashboard_orders'),
    # path('login/', views.login, name='login'),
    path('confirm/', views.SignUpView.as_view(), name='confirm'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('verify_password/', views.verify_password, name='verify_password'),
    path('api/',views.UserListView.as_view())

]