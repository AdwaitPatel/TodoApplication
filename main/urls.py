from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todo/", views.todo, name="todo"),
    path("add_todo/", views.add_todo, name="add_todo"),

    path("remove_task/<int:todo_id>", views.remove_task, name="remove_task"),
    path("update_task/<int:todo_id>", views.update_task, name="update_task"),
    path("complete_task/<int:todo_id>", views.complete_task, name="complete_task"),
    path("update_profile", views.update_profile, name="update_profile"),

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)





