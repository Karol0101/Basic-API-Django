from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import UserProfile
from . serializers import user_serializer


# Create your views here.
class user_list(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializer = user_serializer(users, many=True)
        return Response(serializer.data)

    def post(self):
        pass

    def patch(self):
        pass
