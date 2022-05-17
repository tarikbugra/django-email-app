from django.contrib import admin
from django.urls import path
from .views import IndexView, SendPage

urlpatterns = [
    path('send/', SendPage, name='send'),
    path('', IndexView.as_view(), name='welcome')
]