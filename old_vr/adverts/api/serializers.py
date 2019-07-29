from rest_framework import serializers
from adverts.models import Advert, Order
import datetime


class AdvertSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Advert
        fields = '__all__'


    def get_created_at(self, instance):
        return instance.created_at.strftime("%d-%m-%Y")

    def to_representation(self, instance):
        representation = super(AdvertSerializer, self).to_representation(instance)
        representation['available_from'] = instance.available_from.strftime("%d-%m-%Y")
        representation['available_to'] = instance.available_to.strftime("%d-%m-%Y")
        return representation

    def validate(self, data):
        now = datetime.date.today()
        now.strftime("%d-%m-%Y")
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

    def get_advert_slug(self, instance):
        return instance.advert.slug





    


