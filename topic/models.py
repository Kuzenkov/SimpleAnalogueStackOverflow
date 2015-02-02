# -*- encoding:utf-8 -*-
from django.db import models


class Topic(models.Model):
    """ A class for storing instance topic """
    title = models.CharField(max_length=100)
    question = models.TextField()
    article_date = models.DateTimeField()

    def __unicode__(self):
        return ''.join(self.title)
