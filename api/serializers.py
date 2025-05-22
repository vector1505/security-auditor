from rest_framework import serializers
from .models import SSLAnalysis, SecurityHeaders

class SSLAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSLAnalysis
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class SecurityHeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityHeaders
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
