from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    #path('index/',views.index, name='mainpage'),
    path('register/',views.register, name='register'),
    path('homepage/', views.home, name='home'),
    path('logout/',views.logout, name='logout')

]