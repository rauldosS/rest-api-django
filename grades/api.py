from rest_framework import viewsets

from grades.models import Grades
from grades.serializers import GradesSerializer


class GradesViewSet(viewsets.ModelViewSet):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer