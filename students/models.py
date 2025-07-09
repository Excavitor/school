# students/models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    STATUS_CHOICES = [
        (True, "Active"),
        (False, "Inactive"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    enrolled_class = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    roll = models.PositiveSmallIntegerField(
        default=1, unique=True, validators=[MinValueValidator(1)]
    )
    current_status = models.BooleanField(choices=STATUS_CHOICES, default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
class Review(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='review')

    def __str__(self):
        return self.name
