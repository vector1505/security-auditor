from django.db import models
from django.utils import timezone

class SecurityCheck(models.Model):
    target = models.CharField(max_length=255)
    check_type = models.CharField(max_length=50)
    result = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.check_type} check for {self.target}"

class SSLAnalysis(models.Model):
    target = models.CharField(max_length=255)
    certificate_info = models.JSONField()
    grade = models.CharField(max_length=10)
    vulnerabilities = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SSL Analysis for {self.target}"

class SecurityHeaders(models.Model):
    target = models.CharField(max_length=255)
    headers = models.JSONField()
    security_score = models.IntegerField()
    recommendations = models.JSONField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Security Headers for {self.target}"
