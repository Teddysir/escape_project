from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mouse/', views.mouse, name='mouse'),
    path('main/', views.main, name='main'),
    path('activate/', views.activate, name='activate'),
    
    path('acquire-key/', views.acquire_key, name='acquire_key'),
    path('door1/', views.door1_view, name='door1'),
    path('door2/', views.door2_view, name='door2'),
    path('door3/', views.door3_view, name='door3'),
]
