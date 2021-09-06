from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('krlang/',views.krlang, name='krlang'),
    path('',views.krlang, name='krlang'),
    path('vnlang/',views.vnlang, name='vnlang')
]