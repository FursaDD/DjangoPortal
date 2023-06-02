from django.http import HttpResponse


def index(request):
    return HttpResponse('Скоро здесь будут ответы на частые вопросы.')


def mainpage(request):
    return HttpResponse('Это главная страница нашего корпоративного портала.')
