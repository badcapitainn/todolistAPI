from .models import Todolist
from .serializers import TodolistSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def todolistAPI(request, id = 0):
    if request.method == "GET":
        tasks = Todolist.objects.all()
        tasks_serializer = TodolistSerializer(tasks, many = True)
        return JsonResponse(tasks_serializer.data, safe = False)
    
    elif request.method == "POST":
        task_data = JSONParser().parse(request)
        tasks_serializer = TodolistSerializer(data = task_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse("Task added successfully", safe= False)
        return JsonResponse("Failed to Add Task", safe= False)
    
    elif request.method == "PUT":
        task_data = JSONParser().parse(request)
        task = Todolist.objects.get(id = task_data['id'])
        tasks_serializer = TodolistSerializer(task, data= task_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse("Task Updated", safe= False)
        return JsonResponse("Failed to update Task", safe= False)
    
    elif request.method == "DELETE":
        task = Todolist.objects.get(id = id)
        task.delete()
        return JsonResponse("Task Deleted Successfully", safe= False)
    else:
        return JsonResponse("Invalid Request", safe= False)
 

def is_completed(request, id):
    try:
        task = Todolist.objects.get(id = id)
    except Exception as exception:
        return JsonResponse(f"task not found, {exception}", safe= False)
    
    task.completed = not task.completed
    task.save()
    return JsonResponse(f"completed = {task.completed}", safe = False) 