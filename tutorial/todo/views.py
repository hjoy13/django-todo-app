from django.shortcuts import redirect, render

from .models import Todo

# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        

        if title:
            Todo.objects.create(
                title=title,
                description=description,
                
            )
          

        return redirect("todo_list")

    return  render(request, "todo/list.html", {"todos":todos})


def complete_todo(request,id):
    todo = Todo.objects.get(id=id)
    todo.completed = True
    todo.save()

    return redirect("todo_list")


def edit_todo(request,id):
    todo = Todo.objects.get(id=id)

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