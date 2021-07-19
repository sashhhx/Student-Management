from rest_framework import serializers
from home.models import Marksheet, Student


class MarksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marksheet
        fields = [
            "sub1",
            "sub2",
            "sub3",
            "sub4",
            "sub5"
        ]

class StudentSerializer(serializers.ModelSerializer):
    # result = MarksheetSerializer(read_only=True, many=True)
    class Meta:
        model = Student
        fields = [
            "student_id",
            "student_name",
        ]