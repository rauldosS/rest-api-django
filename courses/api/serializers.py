from rest_framework import serializers
from courses.models import Course, Evaluation

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kargs = {
            'email': {'write_only': True}
        }

        model = Evaluation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'evaluation'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            # 'id',
            'title',
            # 'url',
            # 'creation',
            # 'update',
            # 'active'
        )