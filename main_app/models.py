# main_app/models.py

from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    User = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

class Rental(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    User = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer_user = models.ForeignKey('CustomUser', related_name='buyer_transactions', on_delete=models.CASCADE)
    seller_agent = models.ForeignKey('CustomUser', related_name='seller_transactions', on_delete=models.CASCADE)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

# Define other models such as User, Agent, SearchCriteria, SavedSearch, FavoriteProperty
# Make sure to handle relationships and fields according to your ERD.
