# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 03:10
from __future__ import unicode_literals

from django.db import migrations
from django.utils import timezone

from polls.models import Question, Choice

def load_data(apps, schema_editor):
	q = Question(question_text="Hello world?", pub_date=timezone.now())
	q.save()
	q.choice_set.create(choice_text='Python', votes=1)
	q.choice_set.create(choice_text='Django', votes=1)
	q.choice_set.create(choice_text='Negative votes', votes=-999)
	q = Question(question_text="Do I have a choice?", pub_date=timezone.now())
	q.save()
	q = Question(question_text="Is this question as old as can be?", pub_date="1000-01-01T00:00:00Z")
	q.save()
	q.choice_set.create(choice_text='I\'m pretty sure it is', votes=0)
	q = Question(question_text="Is this question for future generations?", pub_date="2050-01-01T00:00:00Z")
	q.save()
	q.choice_set.create(choice_text='My sources say yes', votes=0)

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
		migrations.RunPython(load_data, hints={'target_db': 'default'}),
    ]
