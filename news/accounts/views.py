from django.contrib.auth import login, views
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import (
    ListView, DetailView, UpdateView, CreateView, DeleteView, RedirectView
)


class NewUser(CreateView):
    template_name = 'accounts/new_account.html'
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('user_details', kwargs={'pk': self.object.id})


class Login(views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class Logout(views.LogoutView):
    template_name = 'accounts/logout.html'
    next_page = 'login'
