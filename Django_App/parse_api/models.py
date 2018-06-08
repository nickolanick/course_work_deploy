from django.db import models


# from

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100,unique=True)
    about = models.CharField(max_length=10000, blank=True)
    average_mark = models.CharField(max_length=10, blank=True)
    comments = models.CharField(max_length=10000, blank=True)
    youtube = models.CharField(max_length=1000,blank=True)
    first_video = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
