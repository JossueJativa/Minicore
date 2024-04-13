from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creatin_date = models.DateTimeField(auto_now_add=False)