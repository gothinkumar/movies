from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=90)
    director = models.CharField(max_length=30)
    image = models.ImageField(upload_to='movieimg')
    desc = models.TextField()

    def __str__(self):
        return self.name