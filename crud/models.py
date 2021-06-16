from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, null=True)
    father = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
    


