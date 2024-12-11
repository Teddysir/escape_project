from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('mouse/', views.mouse, name='mouse'),
    path('main/', views.main, name='main'),
    
    path('activate/', views.activate, name='activate'),
    path('activate/create/', views.create_post, name='create_post'),
    path('activate/<int:post_id>/', views.post_detail, name='post_detail'),
    
    path('door1/', views.door1_view, name='door1'),
    path('door2/', views.door2_view, name='door2'),
    path('door3/', views.door3_view, name='door3'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
