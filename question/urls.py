from django.conf.urls import patterns, include, url
from question import views


urlpatterns = patterns('',
    url(r'^', 'views.QuestionsList.as_view()', name='questions-list'),
)