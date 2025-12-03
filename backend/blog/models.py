from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=16)
    discription = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=16)
    grade = models.PositiveIntegerField()
    attendance = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Price(models.Model):
    name = models.CharField
    discription = models.TextField(blank=True)
    price = models.PositiveIntegerField()  

    def __str__(self):
        return self.name

    





   



