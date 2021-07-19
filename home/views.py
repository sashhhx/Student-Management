from django.db.models.query import QuerySet
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework import serializers, viewsets
from .models import Marksheet, Student
from .forms import MarksheetRegister, StudentRegister
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.serializers import StudentSerializer, MarksheetSerializer
from django.http import JsonResponse

# Create your views here.

@login_required
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('/login')


def marks(request):
    return render(request, 'marks.html')

def timeTable(request):
    return render(request, 'timetable.html')


def timeTableDisplay(request, pk):
    if(pk==1):
        return render(request, 'timetableone.html')

    elif(pk==2):
        return render(request, 'timetabletwo.html')


def marksEnter(request):
    if request.method == "POST":
        form = MarksheetRegister(request.POST)
        student_form = StudentRegister(request.POST)

        if form.is_valid() and student_form.is_valid():
            marksheet = form.save(commit=False)
            student = student_form.save()
            marksheet.student = student
            # marksheet.student_name = student_form.student_name
            marksheet.save()
            return HttpResponseRedirect('/marks')
    return render(request, 'marksenter.html')


def marksDisplay(request):
    stu = Student.objects.all()
    marks = Marksheet.objects.all()
    return render(request, 'marksdisplay.html', {'stu':stu, 'marks':marks})

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class MarksheetViewSet(viewsets.ModelViewSet):
    serializer_class = MarksheetSerializer
    queryset = Marksheet.objects.all()