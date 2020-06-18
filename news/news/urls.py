from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from articles.views import ListArticles


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', ListArticles.as_view(), name="list-articles"),
]

urlpatterns += staticfiles_urlpatterns()
