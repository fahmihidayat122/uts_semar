from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from coret_api.models import coret
from coret_api.serializer import coretserializer

# Create your views here.
@api_view(['GET'])
def coret_list(request):
    corets = coret.objects.all() # Complex Data
    serializer = coretserializer(corets, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def coret_create(request):
    serializer = coretserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)