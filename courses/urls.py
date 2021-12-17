from django.urls import include, path
from .views import CourseAPIView, EvaluationAPIView

app_name = 'courses'

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
]