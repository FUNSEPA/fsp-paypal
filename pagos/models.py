from django.db import models

class Pago(models.Model):
    """
    Description: Pago para funsepa
    """
    number = models.CharField(max_length=16)
    expire_month = models.IntegerField()
    expire_year = models.IntegerField()
    cvv2 = models.CharField(max_length=3)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
    	return str(self.total)