import datetime

from django.test import TestCase
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


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_expired_question(self):
        """
        Questions with a pub_date older than 365 days ago aren't displayed on
        the index page.
        """
        create_question(question_text="Super old question.", days=-100000)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

    def test_expired_question(self):
        """
        The detail view of a question with a pub_date more than a year old
        returns a 404 not found.
        """
        expired_question = create_question(question_text='Expired question.', days=-375)
        url = reverse('polls:detail', args=(expired_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_no_choice_question(self):
        """
        The detail view of a question with no choices will give a relevant message.
        """
        no_choice_question = create_question(question_text='No Choice Question.', days=0)
        url = reverse('polls:detail', args=(no_choice_question.id,))
        response = self.client.get(url)
        self.assertContains(response, 'No choices provided!')

    def test_for_buttons(self):
        """
        The detail view of a question with one choice will contain a radio
        button
        """
        q = create_question(question_text='Question.', days=0)
        q.choice_set.create(choice_text='One choice', votes=0)
        url = reverse('polls:detail', args=(q.id,))
        response = self.client.get(url)
        self.assertContains(response, 'input type="radio"')

class ResultsViewTests(TestCase):

    def test_error(self):
        """
        Error test
        """
        self.assertContains(response, '[THIS TEST SHOULD ERROR]')

    def test_negative_votes(self):
        """
        The detail view of a question with no choices will give a relevant message.
        """
        q = create_question(question_text='Negative Votes Question.', days=0)
        q.choice_set.create(choice_text='Negative votes', votes=-50)
        url = reverse('polls:results', args=(q.id,))
        response = self.client.get(url)
        self.assertContains(response, '(Negative votes)')
        self.assertContains(response, '[THIS TEST SHOULD FAIL]')
