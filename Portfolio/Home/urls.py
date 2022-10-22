from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.index, name='index'),
    path('/about', views.about, name='about'),
    path('/projects', views.projects, name='projects'),
    path('/contact', views.contact, name='contact'),
]
