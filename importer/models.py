from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CsvFile(models.Model):
    file_name = models.FileField(upload_to='csv')
    uploaded = models.DateTimeField(auto_now_add=True)
    # by = models.ForeignKey(User, on_delete=models.CASCADE)
    loaded = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

class ImageZipFile(models.Model):
    file_name = models.FileField(upload_to='zip')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File id: {self.id}"    