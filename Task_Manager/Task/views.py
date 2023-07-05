from django.shortcuts import render
from Task.models import Task


# Create your views here.


def show_index_page(request):
    return render(request, "index.html", context={"Tasks": Task.objects.all()})
