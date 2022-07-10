from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('Encoder/', views.Encoder, name='Encoder'),
    path('Decoder/', views.Decoder, name='Decoder'),
    path('Warn/', views.Warn, name='Warn')
]