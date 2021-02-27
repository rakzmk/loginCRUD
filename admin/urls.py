from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns=[
    path('', views.adlogin, name='admin'),
    path('adminhome/',views.adhome, name='adminhome'),
    path('adlogout/',views.adlogout, name='adlogout'),
    path('delete/<int:id>',views.delete_data, name= 'deletedata'),
    path('update/<int:id>',views.updata_data, name= 'updatedata'),
    path('adminadd/', views.adduser,name='adduser')

]