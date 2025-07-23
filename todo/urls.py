from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('process_add/', views.process_add, name="process_add"),
    path('<int:task_id>/traitement/', views.traitement, name="traitement"),
    path('<int:task_id>/edit/',views.edit, name="edit" ),
]
