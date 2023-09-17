from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    bookID = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100, )
    published_date = models.DateField()
    category = models.ManyToManyField(Category, related_name='category',
                                      default='Other', blank=False)
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='book_pics')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} by {self.authors}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            # resize image
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
