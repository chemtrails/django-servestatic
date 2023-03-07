from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('static/css/<filename>/', views.static_css),
    path('static/js/<filename>/', views.static_js),
    path('static/images/<filename>/', views.static_images)
]