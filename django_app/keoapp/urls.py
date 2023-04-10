from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.keoapp_home,name='keoapp_home'),
]