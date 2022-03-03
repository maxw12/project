from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(days=1)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "no blog are available")
        self.assertQuerysetEqual(response.content['latest_question_list'],[])

    def test_past_question(self):
        question = create_question(question_text="past question", days=-30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question],)

    def test_future_question(self):
        question = create_question(question_text="future question", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, "blog are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        question = create_question(question_text="past question", days=-30)
        # create_question(question_text="future question", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question],)

    def test_two_past_questions(self):
        question1 = create_question(question_text="past question 1", days=-30)
        question2 = create_question(question_text="past Question 2", days=-5)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question2, question1],)

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('blog:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('blog:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)