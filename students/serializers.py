# students/serializers.py

from .models import Student, Review
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'full_name', 'enrolled_class', 'roll', 'current_status', 'created_at']
        read_only_fields = ['id', 'full_name', 'created_at']

    def get_full_name(self, obj):
        first = obj.first_name or ''
        last = obj.last_name or ''
        return f"{first} {last}".strip()
    
class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'student_id']
        read_only_fields = ['id', 'student_id']

    def create(self, validated_data):
        student_id = self.context['student_id']
        return Review.objects.create(student_id = student_id , **validated_data)

