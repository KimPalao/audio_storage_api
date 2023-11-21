from django.db import models

class Audio(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    explicit = models.BooleanField()
    file = models.FileField(upload_to="uploads/")