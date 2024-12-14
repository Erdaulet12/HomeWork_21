from django.db import models

# Create your models here.


class IceCream(models.Model):
    FLAVOR_CHOICES = [
        ('vanilla', 'Vanilla'),
        ('chocolate', 'Chocolate'),
        ('strawberry', 'Strawberry'),
        ('mint', 'Mint'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название")
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES, verbose_name="Вкус")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.name
