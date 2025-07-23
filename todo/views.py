from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Task
from django.urls import reverse

# Create your views here.
def index(request):
    task_list = Task.objects.order_by("dead_line")
    context = {"task_list":task_list}
    return render(request, "todo/index.html", context)


def add(request):
    return render(request, "todo/add.html")

def process_add(request):
    traite = request.POST.get("action")
    if traite == "add":
        descriptif = request.POST.get("description")
        temps = request.POST.get("deadline")
        stat = 0
        task = Task(description= descriptif, dead_line=temps, status=stat)
        task.save()
        return HttpResponseRedirect(reverse("todo:index", args=()))
    
def traitement(request, task_id):
    traite = request.POST.get("action")
    if traite == "delete":
        task = Task.objects.get(pk=task_id)
        task.delete()
        return HttpResponseRedirect(reverse("todo:index", args=()))
    
    elif traite == "save":
        # recuperer les valeurs du formulaire
        descriptif = request.POST.get("description")
        temps = request.POST.get("deadline")
        stat = request.POST.get("status")
        if stat == "on":
            stat = 1
        else:
            stat = 0
        # recuperer la tache a modifier
        task = Task.objects.get(pk=task_id)
        # mettre à jour la base de donénes
        task.description = descriptif
        task.dead_line = temps
        task.status = stat
        task.save()
        return HttpResponseRedirect(reverse("todo:index", args=()))


def edit(request, task_id):
    tache = get_object_or_404(Task, pk=task_id)
    context = {"tache":tache}
    return render(request, "todo/edit.html", context)