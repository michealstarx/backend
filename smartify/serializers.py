from rest_framework import serializers
from .models import Smartify

class SmartifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartify
        fields = '__all__'