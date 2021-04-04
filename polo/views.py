from django.shortcuts import render
from django.http import HttpRequest
from gunicorn import util

def index(request):
    return render(request,'index.html')