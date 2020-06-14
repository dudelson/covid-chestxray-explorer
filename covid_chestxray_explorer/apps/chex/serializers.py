from rest_framework import serializers
from .models import ChestXrayImage


class ChestXrayImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChestXrayImage
        fields = ['id', 'image_url']


class ChestXrayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChestXrayImage
        fields = '__all__'
