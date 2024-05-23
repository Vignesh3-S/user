"""
URL configuration for user_registration_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import Get_All_Users,Get_User,Register_User,Update_User,Delete_User,home

urlpatterns = [
    path('allusers/', Get_All_Users.as_view(),name="allusers"),
    path('create_user/', Register_User.as_view(),name="createuser"),
    path('get_user/<slug:slug>/', Get_User.as_view(),name="getuser"),
    path('updateuser/<slug:slug>/', Update_User.as_view(),name="updateuser"),
    path('delete_user/<slug:slug>/', Delete_User.as_view(),name="deleteuser"),
    path('',home,name="home"),
]
