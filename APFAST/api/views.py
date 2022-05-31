from django.http import HttpResponse
from django.shortcuts import render, redirect

def hello(request): 
    return HttpResponse('Hello World')