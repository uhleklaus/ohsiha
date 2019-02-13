from django.db import models

# Create your models here.

class Text(models.Model):
    textInput = models.CharField(max_length = 100)

    def __str__(self): 
        return self.textInput