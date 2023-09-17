from django.urls import path
from . import views


urlpatterns = [
    path('test/',views.test),
    # path('get-all-todo/',views.get_all_todo),
    # path('create-todo',views.post_todo),
    path('all-todo',views.all_todo),
    path('todo-manipulate/<int:id>',views.todo_maipulate),
]