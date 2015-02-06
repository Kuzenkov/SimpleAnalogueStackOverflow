# -*- encoding:utf-8 -*-
from django.db import models


class Question(models.Model):

    class Meta():
        db_table = "question"

    title = models.CharField(max_length=150)
    question = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return ' '.join(self.title)


class Comments(models.Model):
    """ Contain user comments for question """

    class Meta():
        db_table = "comments"

    comment_text = models.TextField(verbose_name="comment")
    comments_question = models.ForeignKey(Question)
