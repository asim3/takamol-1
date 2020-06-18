from django.contrib.auth import login, views
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import (
    ListView, DetailView, UpdateView, CreateView, DeleteView, RedirectView
)
from .models import Favorite


class NewUser(CreateView):
    template_name = 'accounts/new_account.html'
    model = User
    form_class = UserCreationForm
    success_url = 'list-articles'


class Login(views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class Logout(views.LogoutView):
    template_name = 'accounts/logout.html'
    next_page = 'login'


class ListFavorite(LoginRequiredMixin, ListView):
    template_name = 'articles/list.html'
    paginate_by = 50

    def get_queryset(self):
        id = self.request.user.id
        return Favorite.objects.filter(fk_user__id=id)
