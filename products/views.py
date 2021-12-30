from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from .models import *
from django.conf import settings
from .ApiV1_0 import (ApiProducts)

def getUserIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class insertProduct(APIView):
    def post(self, request, format=None):

        returnData = ApiProducts.insertProduct(self, request.data)
        if returnData['RS'] == "SUCCESS":
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)