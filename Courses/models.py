from django.db import models

# Create your models here.

class Course_List(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    prerequisites = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
