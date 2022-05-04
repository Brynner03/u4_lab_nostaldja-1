from django.db import models

# Create your models here.
class Decades(models.Model):
    start_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year

class Fads(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    description = models.CharField(max_length=250)
    decade = models.CharField(max_length=50)

    def __str__(self):
        return self.name