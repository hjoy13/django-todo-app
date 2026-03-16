from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required 

from .models import Todo

# Create your views here.

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)  

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        

        if title:
            Todo.objects.create(
                user=request.user,
                title=title,
                description=description,
                
            )
          

        return redirect("todo_list")

    return  render(request, "todo/list.html", {"todos":todos})


@login_required
def complete_todo(request,id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.completed = True
    todo.save()

    return redirect("todo_list")


def edit_todo(request,id):
    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")

        todo.title = title
        todo.description = description

        todo.edited = True
        todo.save()
        return redirect("todo_list")
    
    return render(request, "todo/edit.html", {"todo":todo})



def delete_todo(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()

    return redirect("todo_list")