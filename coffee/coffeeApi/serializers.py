from rest_framework import serializers
from .models import Product

class MachineSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sku',
                 'type',
                 'size',
                 'water_line_compatible',
                 'model']

class PodSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sku',
                 'type',
                 'size',
                 'pack_size',
                 'flavor']
