from django.shortcuts import render, redirect, get_object_or_404
from Task.models import Task


# Create your views here.


def show_index_page(request):
    print(Task.sorted_by_name())
    return render(request, "index.html", context={"Tasks": Task.sorted_by_name()})


def show_edit_page(request, id):
    temp = Task.objects.get(pk=id)
    print(temp.Creation_date)
    if request.method == "POST":
        name = request.POST.get("Name")
        description = request.POST.get("Description")
        creation_date = request.POST.get("Creation_date")
        end_date = request.POST.get("End_date")
        priority = request.POST.get("Priority")
        status = request.POST.get("Status")

        temp.Name = name
        temp.Description = description
        temp.Creation_date = creation_date
        temp.End_date = end_date
        temp.Priority = priority
        temp.Status = status
        temp.save()
        return redirect("/")
    return render(request, "edit.html", context={"Task": Task.objects.get(pk=id), "Creation_date": str(Task.objects.get(pk=id).Creation_date), "End_date": str(Task.objects.get(pk=id).End_date)})


def delete(request, id):
    get_object_or_404(Task, pk=id).delete()
    return redirect("/")
