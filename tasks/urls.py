from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet

# from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
   path('', include(router.urls)),
   # path('', views.task, name="task")
]