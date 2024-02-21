from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

# from . import views
from .views import (
    Apihelp,
    DeCoder,
    DecodeViewSet,
    EnCoder,
    EncodeViewSet,
    homepage,
    warning_page,
)

router_encode = routers.DefaultRouter()
router_encode.register(r"upload", EncodeViewSet, basename="upload")
router_decode = routers.DefaultRouter()
router_decode.register(r"upload", DecodeViewSet, basename="upload")

urlpatterns = [
    path("api/", Apihelp.as_view(), name="apidoc"),
    path("api/encode/", include(router_encode.urls)),
    path("api/decode/", include(router_decode.urls)),
    path("", homepage, name="homepage"),
    path("Encoder/", EnCoder.as_view(), name="Encoder"),
    path("Decoder/", DeCoder.as_view(), name="Decoder"),
    path("Warn/", warning_page, name="Warn"),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
