from rest_framework import serializers
from .models import Teacher,Student,Price


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'   

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Price
        fields = '__all__'            