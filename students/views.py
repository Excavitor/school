# students/views.py

from django.shortcuts import render
from .models import Student, Review
from .serializers import StudentSerializers, ReviewSerializers
from rest_framework import viewsets, response, status

def student_list_view(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, 'students/index.html', {'students': students})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def update(self, request, *args, **kwargs):
        student = self.get_object()
        if student.current_status == False:
            return response.Response({'error': 'can not update student because student is not in this school'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        if student.current_status == True:
            return response.Response({'error': 'can not delete student because student is in this school'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializers

    def get_queryset(self):
        return Review.objects.filter(student_id = self.kwargs['student_pk'])
    
    def get_serializer_context(self):
        return {'student_id': self.kwargs['student_pk']}
