from django.forms import fields
from home.models import Marksheet, Student
from django import forms
from django.forms.models import ModelForm
from .models import Student, Marksheet

class StudentRegister(ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_id']


class MarksheetRegister(ModelForm):
    class Meta:
        model = Marksheet
        fields = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5']
