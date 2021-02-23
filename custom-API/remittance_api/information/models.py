from django.db import models

class Trade_information(models.Model):
    bankname = models.CharField(max_length=15)
    account_number = models.IntegerField()
    to_name = models.CharField(max_length = 6)
    from_name = models.CharField(max_length = 6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
