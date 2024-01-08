from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed (e.g., email, designation, etc.)

    def __str__(self):
        return self.name