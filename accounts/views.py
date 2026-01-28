from django.shortcuts import render
from django import views
from django.views.generic import CreateView
from . import forms

# Create your views here.


class SignUpView(views.View):
    def get(self, request):
        form = forms.SignUpForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            obj = form.save()
            return render(request, 'registration/confirm-code.html', {'obj': obj})
        return render(request, 'registration/login.html', {'form': form})

def confirm(request):
    return render(request,'registration/confirm-code.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def dashboard_account(request):
    return render(request,'dashboard/dashboard-account.html')

def dashboard_address(request):
    return render(request,'dashboard/dashboard-address.html')

def dashboard_favorite(request):
    return render(request,'dashboard/dashboard-favorite.html')

def dashboard_messages(request):
    return render(request,'dashboard/dashboard-messages.html')

def dashboard_orders(request):
    return render(request,'dashboard/dashboard-orders.html')

def login(request):
    return render(request,'base.html')

def reset_password(request):
    return render(request,'registration/reset-password.html')


def verify_password(request):
    return render(request,'registration/verify-password.html')