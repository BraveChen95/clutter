# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name=b'\xe8\xa1\xa8\xe9\xa2\x98')),
                ('desc', models.CharField(max_length=200, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('content', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('data_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('link', models.CharField(max_length=200, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
