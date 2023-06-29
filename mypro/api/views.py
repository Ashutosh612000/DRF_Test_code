from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer,UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_get(request):
    if request.method =="GET":
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        json_data = JSONParser().parse(request)
        serializer = StudentSerializer(json_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data ,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)

# def student_get(request,pk):
#     stu = Student.objects.get(id=pk)
#     # print('================================')
#     # print(stu)
#     serializer = StudentSerializer(stu)
#     # print('================================')
#     # print(serializer)
#     # print('================================')
#     # print(serializer.data)
#     # json_data = JSONRenderer().render(serializer.data)
#     # print('================================')
#     # print(json_data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data)


# # Create your views here.
# #Query set -All student
# def student_create(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu , many=True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data,safe = False)

