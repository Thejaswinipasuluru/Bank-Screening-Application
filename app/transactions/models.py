from django.db import models


class Transaction(models.Model):

    transaction_id = models.CharField(max_length=20)

    customer = models.CharField(max_length=100)

    amount = models.DecimalField(max_digits=12, decimal_places=2)

    status = models.CharField(max_length=20)

    def __str__(self):
        return self.transaction_id