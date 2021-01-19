from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('newcontact/', views.newcontact),
    path('viewcontact/<int:pk>/', views.viewcontact),
    path('delete/<int:pk>/', views.delete),
]
