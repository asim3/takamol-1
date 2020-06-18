import requests
from django.conf import settings
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListArticles(LoginRequiredMixin, ListView):
    template_name = 'articles/list.html'
    paginate_by = 20
    extra_context = {'page_title': 'News'}

    def get_queryset(self):
        url = 'https://newsapi.org/v2/everything?q=programing'
        headers = {'X-Api-Key': settings.NEWS_API_KEY}
        news_request = requests.get(url, headers=headers)
        if news_request.status_code == 200:
            response = news_request.json()
            if response.get('status') == "ok":
                return response.get('articles')
        return []
