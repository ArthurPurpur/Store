from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=150, db_index=True)
    body=models.TextField(blank=True)
    price=models.IntegerField()
    cats=models.ManyToManyField('Category', blank=True, related_name='products')
    image=models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-price']



class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})
    
class Order(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    