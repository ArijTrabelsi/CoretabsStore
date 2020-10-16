from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', null=True)

    def get_absolute_url(self):
        return reverse('product_details', args=(self.id,))

    def get_absolute_url_edit(self):
        return reverse('product_edit', args=(self.id,))

    def get_absolute_url_delete(self):
        return reverse('product_delete', args=(self.id,))


    def __str__(self):
        return self.title

