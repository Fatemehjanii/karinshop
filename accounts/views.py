from django.shortcuts import render, redirect
from django import views
from . import forms
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models




# class ArticlesViewSet(ViewSet):
#     def list(self, request):
#         queryset = models.User.objects.all()
#         serializer = serializers.ArticleSerializer(queryset, many=True)
#         return Response(serializer.data)
#     def retrive(self, request, pk=None):
#         queryset = models.User.objects.get(id=pk)
#         serializer = serializers.ArticleSerializer(queryset)
#         return Response(serializer.data)



class SignUpView(views.View):
    def get(self, request):
        form = forms.SignUpForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        email = request.POST.get('email')
        user_model = get_user_model()

        if user_model.objects.filter(email=email).exists():
            request.session['email'] = email
            return redirect('verify_password')
        else:
            form = forms.SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('confirm')
            return render(request, 'registration/login.html', {'form': form})

def verify_password(request):
    if request.method == 'POST':
        form = forms.PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            email = request.session.get('email')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'رمز عبور اشتباه است')
    else:
        form = forms.PasswordForm()
    return render(request, 'registration/verify-password.html', {'form': form})

class UserListView(APIView):
    def get(self, request):
        obj = models.User.objects.all()
        s = serializers.UserListSerializer(obj, many=True)
        return Response(s.data)

def confirm(request):
    return render(request, 'registration/confirm-code.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def dashboard_account(request):
    return render(request, 'dashboard/dashboard-account.html')

def dashboard_address(request):
    return render(request, 'dashboard/dashboard-address.html')

def dashboard_favorite(request):
    return render(request, 'dashboard/dashboard-favorite.html')

def dashboard_messages(request):
    return render(request, 'dashboard/dashboard-messages.html')

def dashboard_orders(request):
    return render(request, 'dashboard/dashboard-orders.html')

def login_view(request):
    return render(request, 'base.html')

def reset_password(request):
    return render(request, 'registration/reset-password.html')
