from rest_framework import serializers


class AssignmentSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True, max_length=256)
    assignment_type = serializers.CharField(read_only=True, max_length=256)
    date = serializers.DateField(read_only=True)
    due_date = serializers.DateField(read_only=True, allow_null=True)
    score = serializers.CharField(read_only=True, max_length=256)
    points = serializers.CharField(read_only=True, max_length=256)
    notes = serializers.CharField(read_only=True, max_length=4096)


class GradeSerializer(serializers.Serializer):
    letter = serializers.CharField(read_only=True, allow_null=True, max_length=8)
    percentage = serializers.CharField(read_only=True, allow_null=True, max_length=8)


class GradesSerializer(serializers.Serializer):
    first_quarter = GradeSerializer(required=False)
    second_quarter = GradeSerializer(required=False)
    third_quarter = GradeSerializer(required=False)
    fourth_quarter = GradeSerializer(required=False)
    first_semester = GradeSerializer(required=False)
    second_semester = GradeSerializer(required=False)
    semester_exam = GradeSerializer(required=False)
    final_exam = GradeSerializer(required=False)


class CourseSerializer(serializers.Serializer):
    period = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True, max_length=256)
    location = serializers.CharField(read_only=True, max_length=256)
    assignments = AssignmentSerializer(required=False, many=True)
    grades = GradesSerializer()
    teacher = serializers.CharField(read_only=True, max_length=128)


class ReportCardSerializer(serializers.Serializer):
    courses = CourseSerializer(many=True)


class QuarterSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    start_date = serializers.DateField(read_only=True)
    end_date = serializers.DateField(read_only=True)
    index = serializers.CharField(read_only=True, max_length=4)
    courses = CourseSerializer(required=False, many=True)


class YearSerializer(serializers.Serializer):
    quarters = QuarterSerializer(many=True)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True, max_length=32)
    full_name = serializers.CharField(read_only=True, max_length=128)
    school_name = serializers.CharField(read_only=True, max_length=256)
    grade = serializers.IntegerField(read_only=True)
    photo = serializers.CharField(read_only=True, max_length=8192)
    schedule = CourseSerializer(many=True)
