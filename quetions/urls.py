
from django.urls import path
from .views import *
urlpatterns = [
    path('',get_answer,name="get_answer"),
    path('answer/<int:n>',get_answer2,name="get_answer2")
]