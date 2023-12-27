from todolist_app import views
from django.urls import path

urlpatterns = [
    path('',views.todolist,name='Todolist'),
    path('delete/<task_id>',views.delete_task,name = 'delete_task'),
    path('edit/<task_id>',views.edit_task,name = 'edit_task'),
    path('complete/<task_id>',views.complete,name = 'complete'),
    path('incomplete/<task_id>',views.incomplete,name = 'incomplete'),
]