from django.db import models

# Create your models here.

class Flights(models.Model):
    source = models.CharField(max_length = 20)
    dest = models.CharField(max_length = 20)

    def __str__(self):
        return self.source