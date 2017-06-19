import datetime

from django.test import TestCase, RequestFactory, mock
from django.urls import reverse
from django.utils import timezone

from .models import Question

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class VoteFormTests(TestCase):
    def test_form_response_code(self):
        """
        The detail view of a question with one choice will contain a radio
        button
        """
        q = create_question(question_text='Question.', days=0)
        q.save()
        q.choice_set.create(choice_text='One choice', votes=0)
        response = self.client.post(
            '/polls/'+str(q.id)+'/vote/',
            {'choice1':'1'}
        )
        q.delete()
        self.assertEqual(response.status_code, 200)
