from .models import Audio
from rest_framework import serializers

class AudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'created_at', 'updated_at', 'name', 'description', 'explicit', 'file']