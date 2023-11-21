from django.shortcuts import render
from .models import Audio
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AudioSerializer

# Create your views here.

class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all().order_by('-created_at')
    serializer_class = AudioSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Audio.objects.all()
        explicit = self.request.query_params.get('explicit')
        if not self.kwargs.get('slug', None) and (explicit is None or explicit == 'false'):
            queryset = queryset.filter(explicit=False)
        queryset = queryset.order_by('-created_at')
        return queryset
