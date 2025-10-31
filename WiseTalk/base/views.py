# this file contains the views or control logic for the base app.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

# room_names = [
#     {'id': 1, 'name': 'Python Programming'},
#     {'id': 2, 'name': 'Django Framework'},
# ]


def home(req):
    print("Home page accessed ->", req)
    room_names = Room.objects.all() 
    context = {'rooms': room_names}
    return render(req, 'base/home.html', context)


def room(req, pk):
    print("Room page accessed ->", req)
    room = Room.objects.get(id=pk)
    context = {'room_name': room}
    return render(req, 'base/room.html', context)
