import os
import datetime
from rest_framework import serializers
from adverts.models import Advert, Order


now = datetime.date.today()
now.strftime("%d-%m-%Y")

class AdvertSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    purchasers_count = serializers.SerializerMethodField()
    availability = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Advert
        exclude = ['purchasers']

    def get_image(self, instance):
        """ Return filename in image url path """
        return os.path.basename(str(instance.image))
        

    def get_purchasers_count(self, instance):
        return instance.purchasers.count()


    def get_availability(self, instance):
        return instance.available_to >= now


    def get_created_at(self, instance):
        return instance.created_at.strftime("%d-%m-%Y")


    def to_representation(self, instance):
        representation = super(AdvertSerializer, self).to_representation(instance)
        representation['available_from'] = instance.available_from.strftime("%d-%m-%Y")
        representation['available_to'] = instance.available_to.strftime("%d-%m-%Y")
        return representation


    def validate(self, data):
        if data['available_from'] > data['available_to']:
            raise serializers.ValidationError("Available to date must occur after available from date")
        elif data['available_to'] < now:
            raise serializers.ValidationError("Ensure that available to date must occur after today or today")
        else:
            return data


class OrderSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    advert_slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = Order
        exclude = ['advert']


    def get_created_at(self, instance):
        return instance.created_at.strftime("%d-%m-%Y")

    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)
        representation['order_from'] = instance.order_from.strftime("%d-%m-%Y")
        representation['order_to'] = instance.order_to.strftime("%d-%m-%Y")
        return representation

    def get_advert_slug(self, instance):
        return instance.advert.slug








    


