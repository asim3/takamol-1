from django.contrib.auth import login, views
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView, DetailView, UpdateView, CreateView, DeleteView, RedirectView
)
from .models import Favorite


class NewUser(CreateView):
    template_name = 'accounts/new_account.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('list-articles')


class Login(views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class Logout(views.LogoutView):
    template_name = 'accounts/logout.html'
    next_page = 'login'


class ListFavorite(LoginRequiredMixin, ListView):
    template_name = 'articles/list.html'
    paginate_by = 50
    extra_context = {'page_title': 'My Favorite'}

    def get_queryset(self):
        id = self.request.user.id
        return Favorite.objects.filter(user_id=id)


class CreateFavoriteView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/login.html'
    model = Favorite
    success_url = reverse_lazy('list-articles')
    fields = ['title', 'author', 'description',
              'url', 'urlToImage', 'publishedAt']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class DeleteFavoriteView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/new_account.html'
    model = Favorite
    success_url = reverse_lazy('list-articles')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(Favorite, id=pk, user=self.request.user)
