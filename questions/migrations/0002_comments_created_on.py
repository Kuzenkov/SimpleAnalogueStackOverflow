# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 10, 8, 37, 1, 827946, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
