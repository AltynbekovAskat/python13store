from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=32)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    have = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    vid = models.FileField(upload_to='vds/', null=True, blank=True)

    def __str__(self):
        return self.product_name
