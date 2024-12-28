from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Product(models.Model):
    """Model representing a product instance"""
    name = models.CharField(
        max_length=200,
        help_text="商品名を入力してください"
    )

    def __str__(self):
        """String for representing the Product"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular product"""
        return reverse("product-detail", args=[str(self.id)])

    class Meta:
        permissions = [('vendor_status', 'Is a vendor')]
        default_permissions = ('add', 'change', 'view')

