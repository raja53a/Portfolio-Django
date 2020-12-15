from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('home/', views.home,name="home"),
]
