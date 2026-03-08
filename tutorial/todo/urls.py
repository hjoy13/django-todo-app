

from .import views
from django.urls import path


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('completed/<int:id>/', views.complete_todo, name='complete_todo'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path("delete/<int:id>/", views.delete_todo, name="delete_todo"),
]