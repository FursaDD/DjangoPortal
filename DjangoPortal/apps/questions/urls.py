from django.urls import path
from . import views


app_name = 'questions'
urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('questions/', views.index, name='index'),
    path('questions/<int:id>/', views.detail, name='detail')
]

