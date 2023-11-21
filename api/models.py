from django.db import models

class Audio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    explicit = models.BooleanField()

    def __str__(self) -> str:
        return self.name

class AudioFile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    file = models.FileField(upload_to="uploads/")
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name="files")
    notes = models.TextField()

    def __str__(self):
        return self.file.path
