from django.db import models

class NexusFile(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file_extension = models.CharField(max_length = 16)

    class Meta:
        ordering = ['name']  # Replace 'id' with your desired default ordering field

    def __str__(self):
        return f"{self.name}.{self.file_extension}"  