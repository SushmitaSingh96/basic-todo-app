from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoItems
# Create your views here.

def todoView(request):
    all_items = ToDoItems.objects.all()
    return render(request,'todo.html',{'key_all_item':all_items})

def addToDo(request):
    new_item=ToDoItems(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteToDo(request, todo_id):
    item_to_delete = ToDoItems.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')