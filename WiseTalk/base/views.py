# this file contains the views or control logic for the base app.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(req):
    print("Home page accessed ->", req)
    return render(req, 'home.html')


def room(req):
    print("Room page accessed ->", req)
    return render(req, 'room.html')
