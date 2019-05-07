from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic

def IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'