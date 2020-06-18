from django.urls import path
from .views import NewUser, Login, Logout, ListFavorite, CreateFavoriteView, DeleteFavoriteView

urlpatterns = [
    path('new/', NewUser.as_view(), name='new_account'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ListFavorite.as_view(), name='profile'),
    path('favorite/', ListFavorite.as_view(), name='favorite-list'),
    path('favorite/new/', CreateFavoriteView.as_view(), name='favorite-new'),
    path('favorite/delete/<int:pk>',
         DeleteFavoriteView.as_view(), name='favorite-delete'),
]
