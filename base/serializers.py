from rest_framework import serializers


class AssignmentSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True, max_length=256)
    assignment_type = serializers.CharField(read_only=True, max_length=256)
    date = serializers.DateField(read_only=True)
    due_date = serializers.DateField(read_only=True, allow_null=True)
    score = serializers.CharField(read_only=True, max_length=256)
    points = serializers.CharField(read_only=True, max_length=256)
    notes = serializers.CharField(read_only=True, max_length=4096)


class CourseSerializer(serializers.Serializer):
    period = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True, max_length=256)
    location = serializers.CharField(read_only=True, max_length=256)
    assignments = AssignmentSerializer(required=False, many=True)
    grade_letter = serializers.CharField(read_only=True, allow_null=True, max_length=4)
    grade_percentage = serializers.CharField(read_only=True, allow_null=True, max_length=16)
    teacher = serializers.CharField(read_only=True, max_length=128)


class QuarterSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    start_date = serializers.DateField(read_only=True)
    end_date = serializers.DateField(read_only=True)
    courses = CourseSerializer(many=True)


class YearSerializer(serializers.Serializer):
    quarters = QuarterSerializer(many=True)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True, max_length=32)
    full_name = serializers.CharField(read_only=True, max_length=128)
    school_name = serializers.CharField(read_only=True, max_length=256)
    grade = serializers.IntegerField(read_only=True)
    photo = serializers.CharField(read_only=True, max_length=8192)
    schedule = CourseSerializer(many=True)
