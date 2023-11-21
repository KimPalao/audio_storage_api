from django.db import models

class Audio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    explicit = models.BooleanField()
    file = models.FileField(upload_to="uploads/")

    def __str__(self) -> str:
        return self.name