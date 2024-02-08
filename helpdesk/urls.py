from django.contrib import admin
from django.urls import path,include
from helpdesk import views

urlpatterns = [
    path('id/',views.helprequest)
]