from django.shortcuts import render
from rest_framework.response import Response
from api.models import Student 
from api.serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class StudentAPi(APIView):

    def get(self, request,pk=None,format=None):
        
        if pk is not None:
            serializer = StudentSerializer(Student.objects.get(id=pk))
            return Response(serializer.data)

        serializer = StudentSerializer(Student.objects.all(),many=True)
        return Response(serializer.data)
    
    def post(self, request,format=None):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            context ={
                'success': True,
                'response': 'Data Created Successfully'
            }
            return Response(context, status=status.HTTP_201_CREATED)
        context = {
            "success":False,
            "response":serializer.errors['name'][0]
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request,pk=None,format=None):
        id = pk 
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial Data Updated Successfully'})
        return Response(serializer.errors)

    def put(self,request,pk=None,format=None):
        id = pk 
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "success":True,
                "response":"data update Successfully"
            }
            return Response(context)
        context ={
            "success":False,
            "response":serializer.errors
        }
        return Response(context)



    def delete(self, request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

# Create your views here.
