from django.shortcuts import render
#Importamos ahorita
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# Create your views here.
class SignUpView(CreateView):
    
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name="registration/signup.html"


def FirstPage(request):

    return render(request,"first_page.html")