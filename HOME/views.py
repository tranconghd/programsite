from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.
def krlang(request):
    return render(request, 'pages/krlang.html')
def vnlang(request):
    return render(request, 'pages/vnlang.html')