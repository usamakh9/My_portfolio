from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(response):
    return HttpResponse('<h1>My site</h1>')
def index(response, id):
    return HttpResponse("<h1>%s<h1/>" %id)

