from django.urls import path
from .views import index, ask_question

urlpatterns = [
    path('', index, name='index'),
    path('ask/', ask_question, name='ask_question'),
]
