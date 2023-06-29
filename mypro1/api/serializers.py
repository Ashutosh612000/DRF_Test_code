from rest_framework import serializers
from api.models import Student

# class StudentSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        