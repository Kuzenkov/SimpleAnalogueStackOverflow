from django.conf.urls import patterns, include, url
import question.views


urlpatterns = patterns('',
    url(r'^', 'question.views.QuestionsList.as_view()', name='questions-list'),
)