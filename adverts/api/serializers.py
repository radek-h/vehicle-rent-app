from rest_framework import serializers
from adverts.models import Advert, Order


class AdvertSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Advert
        fields = '__all__'

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")

    


class OrderSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Order
        exclude = ['advert']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%Y-%m-%d")