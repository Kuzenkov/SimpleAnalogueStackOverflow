# -*- encoding:utf-8 -*-
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Question(models.Model):

    class Meta:
        db_table = "questions"

    title = models.CharField(max_length=150)
    question = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question-view', kwargs={'pk': self.id})


class Answer(models.Model):
    """ Contain user answers for question """
    class Meta:
        db_table = "answers"

    answer_text = models.TextField(verbose_name="answer")
    answers_question = models.ForeignKey(Question)
    created_on = models.DateTimeField(auto_now_add=True)
