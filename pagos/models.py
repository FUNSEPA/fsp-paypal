from django.db import models
from datetime import datetime


class CardType(models.Model):
    card_type = models.SlugField(max_length=25)
    alias = models.CharField(max_length=25)

    def __str__(self):
        return self.alias


class Donnor(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mail = models.EmailField(max_length=150)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Donation(models.Model):
    """
    Description: Pago para funsepa
    """
    card_type = models.ForeignKey(CardType, on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    donnor = models.ForeignKey(Donnor, on_delete=models.PROTECT)
    payment_ref = models.CharField(max_length=225)
    date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.total)
