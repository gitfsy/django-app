from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def keoapp_home(request):
    return HttpResponse('test')