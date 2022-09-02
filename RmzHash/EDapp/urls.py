from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views
from .views import EncodeViewSet, DecodeViewSet

router_encode = routers.DefaultRouter()
router_encode.register(r'upload', EncodeViewSet, basename="upload")
router_decode = routers.DefaultRouter()
router_decode.register(r'upload', DecodeViewSet, basename="upload")

urlpatterns = [
    path('api/', views.Apihelp.as_view(), name='apidoc'),
    path('api/encode/', include(router_encode.urls)),
    path('api/decode/', include(router_decode.urls)),
    path('', views.homepage, name='homepage'),
    path('Encoder/', views.EnCoder.as_view(), name='Encoder'),
    path('Decoder/', views.Decoder, name='Decoder'),
    path('Warn/', views.Warn, name='Warn')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
