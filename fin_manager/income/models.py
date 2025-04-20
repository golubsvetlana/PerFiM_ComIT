from django.db import models
# from django.contrib.auth.models import User


class Income(models.Model):
    CATEGORY_CHOICES = [
        ('Salary', 'Salary'),
        ('Freelance', 'Freelance'),
        ('Business', 'Business'),
        ('Investment', 'Investment'),
        ('Social', 'Social'),
        ('Other', 'Other'),
    ]

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    date = models.DateField(null=True, blank=True)  # <-- Make sure this exists

    def __str__(self):
        return f"{self.source} - {self.amount}"
