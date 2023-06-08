from datetime import timedelta
from django.db import models
# from django.utils import timezone

class CreditsTableList(models.Model):
    courseId=models.IntegerField()
    issueDate = models.DateField()
    expiryDate = models.DateField(editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the instance is being created
            self.expiryDate = self.issueDate + timedelta(days=6*30)  # Add six months (assuming 30 days per month)

        super().save(*args, **kwargs)
        
