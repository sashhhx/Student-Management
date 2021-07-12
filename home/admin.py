from django.contrib import admin
from home.models import Student, Marksheet
# Register your models here.

# class MarksheetAdmin(admin.ModelAdmin):
#     list_display = ['sub1', 'sub2', 'sub3', 'sub4', 'sub5']
    

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'student_name']



admin.site.register(Marksheet)
admin.site.register(Student, StudentAdmin)