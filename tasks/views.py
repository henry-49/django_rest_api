from django.shortcuts import render
from rest_framework import serializers, viewsets, routers
from .models import Task

# Create your views here.
def task(request):
    return render(request, 'tasks/task.html', {})


# Serializers define the API representation.
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at', 'updated_at']

# ViewSets define the view behavior.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

