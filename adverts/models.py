import datetime
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, ValidationError
from .choices import * 
from django.template.defaultfilters import slugify
from VehicleRent.utils import generate_random_string



class Advert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="adverts")
    vehicle_type = models.CharField('Type', choices=VEHICLE_TYPES, max_length=100)
    vehicle_brand = models.CharField('Brand', max_length=100)
    vehicle_model = models.CharField('Model', max_length=100)
    city = models.CharField(max_length=100)
    price_per_day = models.PositiveIntegerField('Price/day', validators=[
                                     MinValueValidator(1)
                                     ])
    available_from = models.DateField()
    available_to = models.DateField()
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)


    # def __str__(self):
    #     return f"USERNAME: {self.author}, {self.vehicle_type.upper()}: {self.vehicle_brand} {self.vehicle_model}"

    def save(self, *args, **kwargs):
        slug = slugify(self.vehicle_brand) + '-' + slugify(self.vehicle_model)
        random_string = generate_random_string()
        self.slug = slug + '-' + random_string
        super(Advert, self).save(*args, **kwargs)

 

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    advert = models.ForeignKey(Advert, 
                                on_delete=models.CASCADE,
                                related_name="orders")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    order_from = models.DateField(default=datetime.date.today)
    order_to = models.DateField()
    comment = models.TextField()

    def __str__(self):
        return f"USERNAME: {self.author.username},  Order from: {self.order_from}, Order to: {self.order_to}"                            



