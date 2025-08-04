from django.db import models

class RVM(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    last_usage = models.DateTimeField()

    def __str__(self):
        return f"{self.location} - {self.status}"
