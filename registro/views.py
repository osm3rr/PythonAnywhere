from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# Create your views here.
class SignUpView(CreateView):
    
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name="registration/signup.html"

class LogoutView(TemplateView):
    template_name = "logout.html"
