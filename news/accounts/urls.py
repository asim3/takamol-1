from django.urls import path
from .views import NewUser, Login, Logout

urlpatterns = [
    path('/new/', NewUser.as_view(), name='new_account'),
    path('/login/', Login.as_view(), name='login'),
    path('/logout/', Logout.as_view(), name='logout'),
]
