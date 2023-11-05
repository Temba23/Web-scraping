from django.db import models

# Create your models here.
class Data(models.Model):
    symbol = models.CharField(max_length=10)
    ltp = models.FloatField(null=True)
    diff = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)    