from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    bookID = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, default='Springer')
    published_date = models.DateField()
    category = models.CharField(max_length=100, default='Business Analytics')
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2)
    # date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.authors}"
    
    objects = models.Manager()