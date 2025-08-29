from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchases")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="purchases")
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.product:
            raise ValueError("Invalid product")
    
        if self.quantity > self.product.stock_quantity:
            raise ValueError("Not enough stock available")

        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

        # Reduce stock
        self.product.stock_quantity -= self.quantity
        self.product.save()


    def __str__(self):
        return f"{self.user.username} bought {self.quantity} of {self.product.name}"
