# this urls file is used to route the requests to appropriate views in the base app.
# this urls file is get the urls and route them to views.py file in base app.


from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
]
