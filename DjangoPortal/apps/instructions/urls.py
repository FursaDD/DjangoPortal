from django.urls import path
from . import views


app_name = 'instructions'
urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('instructions/', views.index, name='index'),
    path('instructions/<int:id>/', views.detail, name='detail')
]

