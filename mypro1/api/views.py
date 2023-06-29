from django.shortcuts import render
import io 
from rest_framework.parsers import JSONParser
from api.serializers import StudentSerializer 
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


# # Create your views here.
# @csrf_exempt
# def student_create(request):
    
#     if request.method == 'POST':
#         json_data = request.body
#         print("======================1==========================")
#         print(request.POST)
#         print("=======================2=========================")
#         print(json_data)
#         stream = io.BytesIO(json_data)
#         print("=========================3=======================")
#         print(stream)
#         pythondata = JSONParser().parse(stream)
#         print("========================4========================")
#         print(pythondata)
#         serilaizer = StudentSerializer(data=pythondata)
#         if serilaizer.is_valid():
#             serilaizer.save()
#             res = {'msg': 'Student created successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer().render(serilaizer.errors)
#         return HttpResponse(json_data, content_type='application/json')

# from rest_framework.views import APIView
# from rest_framework.response import Response

# class Student_create(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             print(data)
#             serdata = StudentSerializer(data=data)
#             if serdata.is_valid():
#                 print("chal rha hain")
#                 serdata.save()

#             context = {
#                 "response": serdata.data
#             }

#             return Response(context)
#         except Exception as e:
#             context = {
#                 "response": str(e)
#             }
#             return Response(context)