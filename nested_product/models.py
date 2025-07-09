from django.db import models

class Product(models.Model):
    STATUS_CHOICE = [
        ('available', 'in stock'),
        ('not_available', 'out of stock'),
    ]
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    product_status = models.CharField(choices=STATUS_CHOICE, default='available')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.name
    
class Review(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.name
