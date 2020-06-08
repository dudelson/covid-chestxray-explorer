from rest_framework import serializers
from .models import ChestXrayImage

class ChestXrayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChestXrayImage
        fields = '__all__'
