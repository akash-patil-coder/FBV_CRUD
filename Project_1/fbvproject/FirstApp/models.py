from django.db import models

# Create your models here.

class Laptop(models.Model):
    company = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    ram = models.IntegerField()
    rom = models.IntegerField()
    processor = models.CharField(max_length=30)
    price = models.IntegerField()
    weigth = models.FloatField()


    def __str__(self):
        return self.company