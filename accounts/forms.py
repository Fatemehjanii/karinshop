from . import models
from django.contrib.auth.forms import UserCreationForm





class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = fields = ('email', 'password1')
        lables = {
            'email':'ایمیل' ,
            'password1':'رمز عبور',
        }


