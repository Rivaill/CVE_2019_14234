from django.http import HttpResponse
from django.shortcuts import render

from TestModel.models import User


def hello(request):
    context = {}
    context['test'] = 'Hello World!'
    return render(request, 'index.html', context)


def select(request):
    context = {}
    context['users']  = User.objects.filter(**request.GET.dict())
    return render(request, 'select.html', context)

def insert(request):
    user = User(info={"name":"rivaill","age":"3"})
    user.save()

    user = User(info={"name":"rivaill2","age":"4"})
    user.save()

    user = User(info={"name":"rivaill3","age":"5"})
    user.save()

    user = User(info={"name":"rivaill4","age":"6"})
    user.save()

    user = User(info={"name":"rivaill5","age":"7"})
    user.save()

    return HttpResponse("<p>success</p>")