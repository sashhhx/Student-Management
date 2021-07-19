from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    student_id = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return self.student_name

class Marksheet(models.Model):
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    sub4 = models.IntegerField()
    sub5 = models.IntegerField()
    student = models.OneToOneField(Student, related_name="result", on_delete=models.CASCADE, null=True)

    # def __str__(self) -> str:
    #     return super().__str__()