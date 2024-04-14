from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                return Response({
                    'status' : 200,
                    'message' : 'Registration successfully check mail',
                    'data' : serializer.data
                })


            return Response({
                'status' : 400,
                'message' : 'Something went wrong',
                'data' : serializer.errors
            })

        except Exception as e:
            print(e)