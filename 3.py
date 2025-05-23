# 3. Model Design and Basic API (20 minutes)
# Task:
# Develop a simple Task Management System from scratch.
# Requirements:
# 1. Create Django models for:
# o User: name, email
# o Task: Ɵtle, descripƟon, assigned_user (ForeignKey), status (Pending, Completed), due_date
# 2. Write a Django REST API endpoint to:
# o POST /tasks/: Create a new task.
# o GET /tasks/?status=Pending: Fetch all tasks filtered by their status.
# 3. Include basic input validaƟon (e.g., ensure due_date is in the future). 



# 1. Create Django models for:
# o User: name, email
# o Task: Ɵtle, descripƟon, assigned_user (ForeignKey), status (Pending, Completed), due_date

from datetime import datetime
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    due_date = models.DateField()

    def __str__(self):
        return self.title
    

from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value < datetime.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        return value
    

# o POST /tasks/: Create a new task. function based view api

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# o GET /tasks/?status=Pending: Fetch all tasks filtered by their status.

@api_view(['GET'])
def get_tasks(request):
    status = request.query_params.get('status')
    if status:
        tasks = Task.objects.filter(status=status)
    else:
        tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)







    