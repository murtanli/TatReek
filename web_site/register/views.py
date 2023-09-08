from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from main.utils import *
from .forms import *
from django.views.generic import CreateView



class sign_up(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, form.instance)
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'signup'
        c_def = self.get_data()
        return dict(list(context.items()) + list(c_def.items()))

class login(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'register/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'login'
        c_def = self.get_data()
        return dict(list(context.items()) + list(c_def.items()))

def logout_user(request):
    logout(request)
    return redirect('home')