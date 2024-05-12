
from django.contrib import admin
from django.urls import path
from coret_api.views import coret_list, coret_create

urlpatterns = [
    path('', coret_create),
    path('list/', coret_list)
]