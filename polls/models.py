import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description = 'Published recently?'

  def is_expired(self):
    now = timezone.now()
    return self.pub_date <= now - datetime.timedelta(days=365)

  is_expired.admin_order_field = 'pub_date'
  is_expired.boolean = True
  is_expired.short_description = 'Expired?'

  def is_future(self):
    now = timezone.now()
    return self.pub_date > now

  is_future.admin_order_field = 'pub_date'
  is_future.boolean = True
  is_future.short_description = 'Future?'


class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
