from django.urls import path, include
from . import views

## PATH Arguments
## 1. Route: the string that contains the url pattern
## 2. View: calls the specified views function
## 3. Name: naming the url allows you to use it all over your site 
## WATCH WHAT YOU NAME YOUR VIEWS/ROUTES

urlpatterns = [
    path('', views.index, name='index'),
    path('forms_output', views.forms_output, name='forms_output')
]