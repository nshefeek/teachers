from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image = models.ImageField(null=True, default='media/profile_pics/default.jpg', upload_to='media/profile_pics')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    room = models.CharField(max_length=200)
    subjects = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"