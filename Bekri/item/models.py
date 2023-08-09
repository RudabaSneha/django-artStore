from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =255)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('name', )
        
    def __str__(self):
        return self.name  
    

class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default = False)
    creator = models.ForeignKey(User, related_name = "items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Items"
    def __str__(self):
        return self.name
    
