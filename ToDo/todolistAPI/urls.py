from django.urls import path
from . import views

urlpatterns = [
    path('todolist', views.todolistAPI),
    path('todolist/<int:id>', views.todolistAPI),
    path('completed/<int:id>', views.is_completed)
]
