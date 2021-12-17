from django.http import JsonResponse
from grades.models import Student
from grades.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, mixins
# GenericViewSet

# class StudentViewSet(viewsets.ModelViewSet):
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # http_method_names = ['get', 'head']

# def grades(request):
#     if request.method == 'GET':
#         students = Student.objects.first()
#         serializer = StudentSerializer(students)

#         return JsonResponse(serializer.data)