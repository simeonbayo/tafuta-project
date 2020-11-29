from django.urls import path, include
from . import views

#Create url patterns here
urlpatterns = [
    path('', views.signup, name = "signup")
]