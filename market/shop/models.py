from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Products'
