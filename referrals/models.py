from django.db import models

# Create your models here.

class ReferralsTable(models.Model):
    referral_id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    