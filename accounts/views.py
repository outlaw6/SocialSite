from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from accounts import forms
from django.views.generic import CreateView
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
