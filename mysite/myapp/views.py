from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.generic import View
import logging
logger = logging.getLogger(__name__)
# ========================================
from .models import Role
import json
from django.http import JsonResponse 
# ========================================
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RoleSerializer
# Create your views here.


# Basic Class based view example
class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')

# User Authentication example
class UserAuthView(View):
    user = authenticate(username="jai", password="password")
    def get(self,request):
        if self.user:
            logger.info('**** User is authentic ****')
            return HttpResponse('User is Authentic !!')
        else:
            logger.info('**** Invalid User / Password ****')
            return HttpResponse('Invalid User / Password ')

# Pure Django Api example
class RoleView(View):
    def get(self, request):
        roles  = Role.objects.first()
        return HttpResponse(json.dumps(roles.dict_rep()), content_type="text/json")
        # return JsonResponse(roles.dict_rep())

class RoleDRFView(APIView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        res_status = status.HTTP_200_OK
        if serializer.is_valid():
            serializer.save()
        else:
            res_status = status.HTTP_400_BAD_REQUEST
        return Response(serializer.data, res_status)


#DRF API example
class UserView(APIView):

    def get(self,request,format=None):
        return Response(data, status=status.HTTP_200_OK)

