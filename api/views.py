from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import SSLAnalysis, SecurityHeaders, SecurityCheck
from .serializers import SSLAnalysisSerializer, SecurityHeadersSerializer
from .services import SSLAnalysisService, SecurityHeadersService, MalwareCheckService, NetworkScanService, DNSCheckService

class SSLAnalysisViewSet(viewsets.ModelViewSet):
    queryset = SSLAnalysis.objects.all()
    serializer_class = SSLAnalysisSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def analyze(self, request):
        target = request.data.get('target')
        if not target:
            return Response({'error': 'Target is required'}, status=status.HTTP_400_BAD_REQUEST)

        service = SSLAnalysisService()
        result = service.analyze(target)
        
        analysis = SSLAnalysis.objects.create(
            target=target,
            certificate_info=result.get('certificate_info', {}),
            grade=result.get('grade', ''),
            vulnerabilities=result.get('vulnerabilities', {})
        )
        
        serializer = self.get_serializer(analysis)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SecurityHeadersViewSet(viewsets.ModelViewSet):
    queryset = SecurityHeaders.objects.all()
    serializer_class = SecurityHeadersSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def check(self, request):
        target = request.data.get('target')
        if not target:
            return Response({'error': 'Target is required'}, status=status.HTTP_400_BAD_REQUEST)

        service = SecurityHeadersService()
        result = service.check(target)
        
        headers = SecurityHeaders.objects.create(
            target=target,
            headers=result.get('headers', {}),
            security_score=result.get('score', 0),
            recommendations=result.get('recommendations', [])
        )
        
        serializer = self.get_serializer(headers)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MalwareCheckViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        target = request.data.get('target')
        if not target:
            return Response({'error': 'Target is required'}, status=status.HTTP_400_BAD_REQUEST)

        service = MalwareCheckService()
        result = service.check(target)
        
        security_check = SecurityCheck.objects.create(
            target=target,
            check_type='malware',
            result=result
        )
        
        return Response(result, status=status.HTTP_201_CREATED)

class NetworkScanViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        target = request.data.get('target')
        if not target:
            return Response({'error': 'Target is required'}, status=status.HTTP_400_BAD_REQUEST)

        service = NetworkScanService()
        result = service.scan(target)
        
        security_check = SecurityCheck.objects.create(
            target=target,
            check_type='network',
            result=result
        )
        
        return Response(result, status=status.HTTP_201_CREATED)

class DNSCheckViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        target = request.data.get('target')
        if not target:
            return Response({'error': 'Target is required'}, status=status.HTTP_400_BAD_REQUEST)

        service = DNSCheckService()
        result = service.check(target)
        
        security_check = SecurityCheck.objects.create(
            target=target,
            check_type='dns',
            result=result
        )
        
        return Response(result, status=status.HTTP_201_CREATED)
