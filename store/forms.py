from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2']
        labels = {'full_name': 'Full Name',
                  }
        
        