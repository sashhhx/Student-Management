from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    student_id = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.student_name

class Marksheet(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    sub4 = models.IntegerField()
    sub5 = models.IntegerField()
