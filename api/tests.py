from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import SSLAnalysis, SecurityHeaders
from .services import SSLAnalysisService, SecurityHeadersService

class SecurityAnalysisTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ssl_service = SSLAnalysisService()
        self.headers_service = SecurityHeadersService()

    def test_ssl_analysis(self):
        """Test SSL certificate analysis"""
        target = "example.com"
        response = self.client.post(
            reverse('ssl-analysis-list'),
            {'target': target},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('grade', response.data)
        self.assertIn('vulnerabilities', response.data)

    def test_security_headers(self):
        """Test security headers analysis"""
        target = "example.com"
        response = self.client.post(
            reverse('security-headers-list'),
            {'target': target},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('security_score', response.data)
        self.assertIn('recommendations', response.data)

    def test_malware_check(self):
        """Test malware/phishing detection"""
        target = "example.com"
        response = self.client.post(
            reverse('malware-check-list'),
            {'target': target},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('malware_detected', response.data)
        self.assertIn('phishing_detected', response.data)

    def test_network_scan(self):
        """Test network scanning"""
        target = "192.168.1.1"
        response = self.client.post(
            reverse('network-scan-list'),
            {'target': target},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('open_ports', response.data)
        self.assertIn('vulnerabilities', response.data)

    def test_dns_check(self):
        """Test DNS security checks"""
        target = "example.com"
        response = self.client.post(
            reverse('dns-check-list'),
            {'target': target},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('dnssec', response.data)
        self.assertIn('spf', response.data)
        self.assertIn('dmarc', response.data)
