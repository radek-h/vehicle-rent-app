from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from .choices import * 
from datetime import date



class Advert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="adverts")
    vehicle_type = models.CharField(choices=VEHICLE_TYPES, max_length=100)
    vehicle_brand = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price_per_day = models.FloatField(validators=[
                                     MinValueValidator(0.1)
                                     ])
    available_from = models.DateField(default=date.today)
    available_to = models.DateField()
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return f"USERNAME: {self.author}, {self.vehicle_type.upper()}: {self.vehicle_brand} {self.vehicle_model}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    advert = models.ForeignKey(Advert, 
                                on_delete=models.CASCADE,
                                related_name="orders")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    order_from = models.DateField(default=date.today)
    order_to = models.DateField()
    comment = models.TextField()

    # def get_order_from(self):
    #     return self.advert.available_from

    def __str__(self):
        return f"USERNAME: {self.author.username},  Order from: {self.order_from}, Order to: {self.order_to}"                            



