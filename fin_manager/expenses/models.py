from django.db import models
# from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('health', 'Health'),
        ('beauty', 'Beauty'),
        ('entertainment', 'Entertainment'),
        ('study', 'Study'),
        ('rent', 'Rent'),
        ('utility', 'Utility'),
        ('transport', 'Transport')
    ]

    name = models.CharField(max_length=255, default='other')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.category} - ${self.amount}"

