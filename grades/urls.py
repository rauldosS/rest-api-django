from django.urls import include, path
from . import views

app_name = 'grades'

urlpatterns = [
    path('', views.grades, name='home'),
]