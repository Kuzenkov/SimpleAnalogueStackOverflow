from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, ModelFormMixin, ProcessFormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from questions.models import Question, Answer
from forms import AnswerForm, QuestionForm


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class QuestionsList(ListView):
    """ Class for displaying list of questions """
    model = Question
    paginate_by = 10
    template_name = 'question_list.html'


class QuestionView(DetailView, ModelFormMixin, ProcessFormView):
    """
    Class for displaying page with question, answers and form for giving answer
    """
    model = Question
    form_class = AnswerForm
    template_name = 'question.html'

    def get_success_url(self):
        return reverse('question-view', kwargs={'pk': self.get_object().pk})

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(answers_question_id=self.get_object())
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        self.object = Answer(answers_question_id=self.get_object().pk)
        return super(QuestionView, self).post(request, *args, **kwargs)


class QuestionCreate(LoggedInMixin, CreateView):
    model = Answer
    template_name = 'new_question.html'
    form_class = QuestionForm

    def get_initial(self):
        self.initial.update({'owner': self.request.user})
        return self.initial
