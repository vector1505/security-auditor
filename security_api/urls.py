from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import SSLAnalysisViewSet, SecurityHeadersViewSet, MalwareCheckViewSet, NetworkScanViewSet, DNSCheckViewSet

router = routers.DefaultRouter()
router.register(r'ssl-analysis', SSLAnalysisViewSet, basename='ssl-analysis')
router.register(r'security-headers', SecurityHeadersViewSet, basename='security-headers')
router.register(r'malware-check', MalwareCheckViewSet, basename='malware-check')
router.register(r'network-scan', NetworkScanViewSet, basename='network-scan')
router.register(r'dns-check', DNSCheckViewSet, basename='dns-check')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
