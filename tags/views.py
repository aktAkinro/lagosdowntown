from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from tags.models import TaggedItem
from .serializers import TaggeditemSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models.aggregates import Count

# Create your views here.


@swagger_auto_schema(methods=['POST'], request_body=TaggeditemSerializer())
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def tagged_items(request):
    if request.method == 'GET':
        queryset = TaggedItem.objects.annotate(products_count=Count('id')).all()
        serializer = TaggeditemSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaggeditemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
