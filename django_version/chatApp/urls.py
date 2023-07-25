from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('solveIt/api/<isAuth>/',views.dummy_home),
    path('',views.home,name='home'),
    path('login',views.login_user,name='login'),
    path('signup',views.signup_user,name="signup"),
    path('sent_msg',views.sent_msg,name='sent_msg'),
    
    
    path('chats',views.chats_show,name='chats'),
    path('dontknow/chats',views.chat,name='dontknow'),
    
]