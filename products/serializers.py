from dataclasses import fields
import imp
from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['title','description', 'price', 'inventory_quantity' ]