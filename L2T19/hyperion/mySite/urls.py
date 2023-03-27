from django.urls import path, include
from . import views
from register import views as v

app_name = 'mySite'
urlpatterns = [
path('index', views.index, name='index'),
path('about', views.about, name='about'),
path('', v.register, name='register'),
path('register', v.register, name='register'),
path('contact/', views.contact, name='contact'),

]