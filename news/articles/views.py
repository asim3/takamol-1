import requests
from django.views.generic import ListView
from django.conf import settings


class ListArticles(ListView):
    template_name = 'articles/list.html'
    paginate_by = 20

    def get_queryset(self):
        url = 'https://newsapi.org/v2/everything?q=programing'
        headers = {'X-Api-Key': settings.NEWS_API_KEY}
        news_request = requests.get(url, headers=headers)
        if news_request.status_code == 200:
            response = news_request.json()
            if response.get('status') == "ok":
                return response.get('articles')
        print("\n\n\n----------", news_request.status_code)
        return []
