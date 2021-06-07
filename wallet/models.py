from django.db import models


class Wallet(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(balance__gte=0), name='Min value 0')
        ]


class Transaction(models.Model):
    from_wallet = models.ForeignKey('wallet.Wallet', on_delete=models.CASCADE, null=True, related_name='from_wallet')
    to_wallet = models.ForeignKey('wallet.Wallet', on_delete=models.CASCADE, null=True, related_name='to_wallet')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)