# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.TextField(verbose_name=b'answer')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('answers_question', models.ForeignKey(to='questions.Question')),
            ],
            options={
                'db_table': 'answers',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comments_question',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
