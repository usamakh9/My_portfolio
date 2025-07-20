from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist, Item
# Create your views here.


def home(response):
    return render('response', 'main/home.html', {})

def index(response, id):
    ls = Todolist.objects.get(id=id)
    return render('response', 'main/list.html', {'ls':ls})

