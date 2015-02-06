from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from questions.models import Question


class QuestionsList(ListView):
    """ Class for displaying list of questions """
    model = Question
    template_name = 'question_list.html'
    context['title'] = 'title'


class QuestionView(DetailView):
    model = Question
    template_name = 'question.html'