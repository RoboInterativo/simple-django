from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    prod_date = models.DateTimeField('date published')
    price= models.FloatField()

    # pub_date = models.DateTimeField('date published')


# Create your models here.
