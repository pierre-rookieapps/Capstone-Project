from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    nb_of_guests = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(6),
            MinValueValidator(1)
        ]
    )
    booking_date = models.DateField()

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )