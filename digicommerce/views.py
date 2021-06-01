from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'base.html')
def produto(request):
    return render(request, 'produto.html')
