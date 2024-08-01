from django.shortcuts import render, redirect
from .models import Todo, Profile


# =================================== HOME ==============================

def home(request):
    return render(request, "home.html")


# =================================== Todo ==============================


def todo(request):

    user = request.user

    #========================= main section ============

    todos = Todo.objects.all()

    incomplete_todos = todos.filter(is_completed = False)    

    completed_todos = todos.filter(is_completed = True)

    context = {
        "todos": incomplete_todos,
        "completed_todos": completed_todos,
        "user": user
    }

    return render(request, "todo.html", context)


# =================================== ADD Todo ==============================


def add_todo(request):

    if request.method == "POST":

        todo = request.POST.get("task")
        date = request.POST.get("date")

        create_todo = Todo(task = todo, date = date)
        create_todo.save()

        return redirect("todo")


    return render(request, "add_todo.html")


# =================================== DELETE Todo ============================


def remove_task(request, todo_id):
    
    remove_task = Todo.objects.get(id = todo_id)
    remove_task.delete()

    return redirect("todo")



# ================================= Update Todo ==========================================


def update_task(request, todo_id):

    todo = Todo.objects.get(id = todo_id)

    context = {
        "todo": todo
    }

    if request.method == "POST":

        updated_task = request.POST.get("updated_task")
        date = request.POST.get("date")

        todo.task = updated_task
        todo.date = date

        todo.save()

        return redirect("todo")

    return render(request, "update_task.html", context)



# ================================== Complete Todo ==========================================


def complete_task(request, todo_id):

    todo = Todo.objects.get(id = todo_id)

    todo.is_completed = True

    todo.save()
    
    return redirect("todo")



# ================================== Update Profile ==========================================

def update_profile(request):
    
    if request.method == "POST":
        # profile_pic = request.POST.get("profile_pic") #  get give only text data

        profile_pic = request.FILES["profile_pic"]

        new_profile = Profile(
            title = "demo title",
            profile_pic = profile_pic
        )

        new_profile.save()

        return redirect("todo")
    
    return render(request, "update_profile_pic.html")

