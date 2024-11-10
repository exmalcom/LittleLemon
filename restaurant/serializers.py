from rest_framework import serializers
from .models import MenuItem
from .models import Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'  # Include all fields of the MenuItem model

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # This will include all fields in the Booking model
