from django.db import models

class Trade(models.Model):
    category = models.CharField(max_length = 15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
