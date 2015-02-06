from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from question.model import Question


class QuestionsView(ListView):
    """ Class for displaying list of questions """
    model = Question
    template_name = 'question_list.html'