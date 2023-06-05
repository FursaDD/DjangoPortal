from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from django.http import Http404


def index(request):
    latest_questions = Question.objects.order_by('-id')

    return render(request, 'questions/list.html', {'questions': latest_questions})


def mainpage(request):
    return render(request, 'base.html')


def detail(request, id):
    try:
        question = Question.objects.get(id=id)
    except Exception:
        raise Http404('Ой, кажется, такой страницы нет.')
    return render(request, 'questions/question.html ', {'question': question})