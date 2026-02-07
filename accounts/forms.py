from . import models
from django.contrib.auth.forms import UserCreationForm
from django import forms





class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = fields = ('email', 'password1')
        lables = {
            'email':'ایمیل' ,
            'password1':'رمز عبور',
        }


class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'p-3 w-full sm:text-sm/6 text-base appearance-none text-gray-800 dark:text-gray-100'}))

