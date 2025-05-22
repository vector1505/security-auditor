from django.contrib import admin
from .models import SecurityCheck, SSLAnalysis, SecurityHeaders

@admin.register(SecurityCheck)
class SecurityCheckAdmin(admin.ModelAdmin):
    list_display = ('target', 'check_type', 'created_at')
    list_filter = ('check_type', 'created_at')
    search_fields = ('target',)

@admin.register(SSLAnalysis)
class SSLAnalysisAdmin(admin.ModelAdmin):
    list_display = ('target', 'grade', 'created_at')
    list_filter = ('grade', 'created_at')
    search_fields = ('target',)

@admin.register(SecurityHeaders)
class SecurityHeadersAdmin(admin.ModelAdmin):
    list_display = ('target', 'security_score', 'created_at')
    list_filter = ('security_score', 'created_at')
    search_fields = ('target',)
