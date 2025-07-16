from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist, Item
# Create your views here.


def home(response):
    return HttpResponse('<h1>My site</h1>')

def index(response, id):
    ls = Todolist.objects.get(id=id)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s<h1/><br><br>" %str(items.text))

