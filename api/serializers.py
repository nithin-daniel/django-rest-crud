from rest_framework import serializers
from .models import Item , Locations

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('__all__')