from .models import ChestXrayImage
from .serializers import ChestXrayImageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ChestXrayImageList(APIView):
    def get(self, request, format=None):
        images = ChestXrayImage.objects.all()
        serializer = ChestXrayImageSerializer(images, many=True)
        return Response(serializer.data)


class ChestXrayImageDetail(APIView):
    def get_object(self, pk):
        try:
            return ChestXrayImage.objects.get(pk=pk)
        except ChestXrayImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        image = self.get_object(pk)
        serializer = ChestXrayImageSerializer(image)
        return Response(serializer.data)
