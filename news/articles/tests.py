from django.test import TestCase
import requests
from django.conf import settings


class AnimalTestCase(TestCase):
    def test_newsapi_key(self):
        url = 'https://newsapi.org/v2/everything?q=programing'
        headers = {'X-Api-Key': settings.NEWS_API_KEY}
        news_request = requests.get(url, headers=headers)

        self.assertEqual(200, news_request.status_code)
        self.assertEqual("ok", news_request.json().get('status'))
