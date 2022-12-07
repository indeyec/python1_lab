from django.urls import path
from . import views
from .views import ChangeUserInfoView
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("profile/account/", views.accountSettings, name="account"),
    path('all/', views.AllView.as_view(), name='all'),
    path('profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
]
