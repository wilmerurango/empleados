from django.shortcuts import render
from django.views.generic import  CreateView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def login(request):
    return render(request, 'login-simple.html',{})

def form(request):
    return render(request, 'form.html',{})

def list_user(request):
    userr = User.objects.all()
    return render(request, 'list_user.html',{'users':userr})


class Crear_User(CreateView): #crear usuario
    model = User
    template_name = 'crear_user.html'
    form_class = UserForm
    success_url = reverse_lazy('index')