# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20150211_0703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-created_on']},
        ),
    ]
