from django.test import TestCase, LiveServerTestCase
from questions.models import Question, Answer
from questions.views import QuestionsList, QuestionView
from django.contrib.auth.models import User
from questions import signals
from django.test import Client
from django.test.client import RequestFactory
from selenium.webdriver.firefox.webdriver import WebDriver

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock

client = Client()


class QuestionsTest(TestCase):
    """ Tests for Question's model methods """

    def test_str(self):
        question = Question(title='test_title',  question='asasdasdas')
        self.assertEquals(
            str(question),
            'test_title',
        )

    def test_get_absolute_url(self):
        question = Question(title='test_title',  question='asasdasdas', owner_id=1)
        question.save()
        resp = self.client.get(question.get_absolute_url())
        self.assertEquals(resp.status_code, 200)


class QuestionsListTests(TestCase):
    """Questions list view tests."""

    def test_contacts_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = QuestionsList.as_view()(request)
        self.assertEquals(list(response.context_data['object_list']), [])

        Question.objects.create(title='test_title',  question='asasdasdas', owner_id=1)
        response = QuestionsList.as_view()(request)
        self.assertEquals(len(response.context_data['object_list']), 1)


class QuestionViewTests(TestCase):
    """Question view tests."""

    def test_question_display(self):
        """ """
        factory = RequestFactory()
        question = Question(title='test_title',  question='asasdasdas', owner_id=1)
        question.save()
        request = factory.get('/')

        response = QuestionView.as_view()(request, pk=question.pk)
        self.assertEquals(response.context_data['question'].title, 'test_title')
        self.assertEquals(response.context_data['question'].question, 'asasdasdas')

    def test_form_should_post_proper_data_via_signal(self):
        """ test signal sending message if added a comment """
        mock_handler = MagicMock()

        user = User.objects.create_user(username='John', email='John@test.com', password='password')
        user.save()
        question = Question(title='test_title',  question='asasdasdas', owner_id=1)
        question.save()
        answer = Answer(answer_text='some_text', answers_question=question)
        answer.save()

        signals.post_save.connect(mock_handler, sender=Answer)

        signals.post_save.send(sender=Answer, instance=question, answer=answer.answer_text)

        # handler.assert_called_once_with(
        #                                  signal=signals.post_save.send,
        #                                  sender=Answer,
        #                                  instance=question,
        #                                  answer=answer.answer_text)
        self.assertEquals(mock_handler.call_count, 1)


class QuestionListIntegrationTests(LiveServerTestCase):
    """  """
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(QuestionListIntegrationTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(QuestionListIntegrationTests, cls).tearDownClass()

    def test_question_listed(self):
        """ Test for check dispaying question title """
        # create a test question
        user = User.objects.create_user(username='John', email='John@test.com', password='password')
        user.save()

        Question.objects.create(title='test_title',  question='asasdasdas', owner_id=user.pk)

        # make sure it's listed as <first> <last> on the list
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.title')[0].text,
            'test_title'
        )

    def test_add_question_linked(self):
        """ Test for check button 'Ask question' """
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.assert_(
            self.selenium.find_element_by_link_text('Ask question')
        )

    def test_add_question(self):

        self.selenium.get('%s%s' % (self.live_server_url, '/new-question/'))

        self.selenium.find_element_by_id('id_title').send_keys('test_tt')
        self.selenium.find_element_by_id('id_question').send_keys('question')

        ell = self.selenium.find_element_by_id("question_form")
        ell.click()

        self.assertEqual(
            self.selenium.find_elements_by_css_selector('.title')[-1].text,
            'test_tt'
        )
