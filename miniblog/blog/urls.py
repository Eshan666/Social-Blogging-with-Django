from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('loginPage/' ,views.loginPage,name="loginPage"),
    path('logoutPage/' ,views.logoutPage,name="logoutPage"),
    path('signupPage/' ,views.signupPage,name="signupPage"),
    path('aboutPage/' ,views.aboutPage,name="aboutPage"),
    path('contactPage/' ,views.contactPage,name="contactPage"),
    path('dashBoardPage/' ,views.dashBoardPage,name="dashBoardPage"),
    path('myProfilePage/' ,views.myProfilePage,name="myProfilePage"),
    path('updatePost/<str:pk>/' ,views.updatePost,name="updatePost"),
    path('deletePost/<str:pk>/' ,views.deletePost,name="deletePost"),
    
]