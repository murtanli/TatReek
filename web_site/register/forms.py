from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Enter your name', widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'passwordInput'}))
    password2 = forms.CharField(label='Again enter password', widget=forms.PasswordInput(attrs={'placeholder': 'Again enter password','id':'passwordInput2'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(RegisterUserForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'passwordInput'}))