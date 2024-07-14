from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_urls/', views.view_urls, name='view_urls'),
    path('<str:short_url>/', views.redirect_to_original, name='redirect'),
]
