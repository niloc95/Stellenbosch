from django.urls import path, include
from . import views
urlpatterns = [
path('', views.index),
path('nilo/', views.nilo, name='nilo'),
]