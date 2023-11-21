from .models import Audio, AudioFile
from rest_framework import serializers

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ['id', 'file']

class AudioSerializer(serializers.ModelSerializer):
    files = AudioFileSerializer(read_only=True, many=True)

    class Meta:
        model = Audio
        fields = ['id', 'created_at', 'updated_at', 'name', 'slug', 'description', 'explicit', 'files']
        read_only_fields  = ['id', 'created_at', 'updated_at', 'name', 'slug', 'description', 'explicit', 'files']
