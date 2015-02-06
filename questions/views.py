from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from question.models import Question


class QuestionsList(ListView):
    """ Class for displaying list of questions """
    model = Question
    template_name = 'question_list.html'