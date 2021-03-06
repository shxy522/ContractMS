# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-19 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0009_remove_role_fun7'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='approval2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='a2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='administration',
            name='approval3',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='a3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='administration',
            name='atime1',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='atime2',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='atime3',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='countersign2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='administration',
            name='countersign3',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='administration',
            name='ctime1',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='ctime2',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='ctime3',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='option1',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='option2',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='option3',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='sinformation',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='administration',
            name='stime',
            field=models.DateField(default=None, null=True),
        ),
    ]
