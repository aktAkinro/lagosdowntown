from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from likes.models import LikedItem
from .serializer import LikeditemSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models.aggregates import Count

# Create your views here.


@swagger_auto_schema(methods=['POST'], request_body=LikeditemSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def liked_items(request):
    if request.method == 'GET':
        queryset = LikedItem.objects.annotate(products_count=Count('id')).all()
        serializer = LikeditemSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LikeditemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
