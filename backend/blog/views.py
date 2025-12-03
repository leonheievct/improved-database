from .models import Teacher,Student,Price
from .serializers import TeacherSerializer,StudentSerializer,PriceSerializer
from rest_framework import viewsets

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = StudentSerializer

class PriceViewSet(viewsets.ModelViewSet):
        queryset = Price.objects.all() 
        serializer_class = PriceSerializer     

        

