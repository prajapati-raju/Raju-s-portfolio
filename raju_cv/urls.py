from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home_page'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('qualification/', views.qualification, name='qualification'),
]