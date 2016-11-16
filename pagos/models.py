from django.db import models


class CardType(models.Model):
    card_type = models.SlugField(max_length=25)
    alias = models.CharField(max_length=25)

    def __str__(self):
        return self.alias


class Donnor(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mail = models.EmailField(max_length=150)

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

    def __str__(self):
        return str(self.total)
