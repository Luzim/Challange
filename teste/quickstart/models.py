from django.db import models

# Create your models here.
class Phrase(models.Model):
    phrase = models.CharField(max_length=30)
    def __str__(self):
        return self.phrase