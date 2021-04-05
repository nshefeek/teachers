from django.db import models

class MultipleFiles(models.Model):
    csv_file = models.FileField(upload_to='csv')
    zip_file = models.FileField(upload_to='zip')
    csv_activated = models.BooleanField(default=False)
    zip_extracted = models.BooleanField(default=False)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File id: {self.id}"
