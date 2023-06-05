from django.http import HttpResponse
from django.shortcuts import render
from .models import Instruction
from django.http import Http404


def index(request):
    latest_instructions = Instruction.objects.order_by('-instruction_create_date')

    return render(request, 'instructions/list.html', {'instructions': latest_instructions})


def mainpage(request):
    return render(request, 'base.html')


def detail(request, id):
    try:
        instruction = Instruction.objects.get(id=id)
    except Exception:
        raise Http404('Ой, кажется, такой страницы нет.')
    return render(request, 'instructions/instruction.html ', {'instruction': instruction})
