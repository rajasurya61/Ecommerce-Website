from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length=255)  # Name of the category

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField()  # Description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Foreign key to Category

    def __str__(self):
        return self.name

# Review model
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Foreign key to Product
    rating = models.IntegerField()  # Rating given to the product
    comment = models.TextField()  # Comment about the product
    user_id = models.IntegerField()  # ID of the user who wrote the review

    def __str__(self):
        return f'Review of {self.product.name}'


class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)