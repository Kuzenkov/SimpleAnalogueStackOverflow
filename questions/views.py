from django.shortcuts import render, render_to_response, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, ModelFormMixin, ProcessFormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from questions.models import Question, Answer
from forms import AnswerForm, QuestionForm
from questions import signals


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class QuestionsList(ListView):
    """ Class for displaying list of questions """
    model = Question
    template_name = 'question_list.html'

    def get_queryset(self):
        question_list = Question.objects.all()

        paginator = Paginator(question_list, 10)
        page = self.request.GET.get('page')

        try:
            questions = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            questions = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            questions = paginator.page(paginator.num_pages)
        return questions


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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.answers_question_id = self.get_object().pk
        self.object.save()
        signals.post_save.send(sender=Answer, instance=self.get_object(), answer=self.object.answer_text)
        return HttpResponseRedirect(self.get_success_url())


class QuestionCreate(LoggedInMixin, CreateView):
    model = Answer
    template_name = 'new_question.html'
    form_class = QuestionForm

    def get_success_url(self):
        return reverse('question-view', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    # another method create object with owner parameter
    """def get_initial(self):
        self.initial.update({'owner': self.request.user})
        return self.initial
    """
