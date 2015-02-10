from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from questions.models import Question, Comments


class QuestionsList(ListView):
    """ Class for displaying list of questions """
    model = Question
    paginate_by = 10
    template_name = 'question_list.html'


class QuestionView(DetailView):
    model = Question
    template_name = 'question.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(comments_question_id=self.get_object().pk)
        return context
