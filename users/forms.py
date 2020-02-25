from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'Enter your name here'
                                                                               }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter your surname here'
                                                                              }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'example@mail.com'
                                                            }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'password'
                                                                                    }))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'the same password once more'
                                                                                    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@mail.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your password'
    }))
