# -*- encoding:utf-8 -*-
from django.conf.urls import patterns, include, url
import questions.views


urlpatterns = patterns(
    '',
    url(r'^$', questions.views.QuestionsList.as_view(), name='questions-list'),
    url(r'^(?P<pk>\d+)/$', questions.views.QuestionView.as_view(), name='question-view'),
    url(r'^new-question/$', questions.views.QuestionCreate.as_view(), name='new-question'),
)
