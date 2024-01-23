from django.urls import path,include
from .views import RegisterView , GoogleLogin,home

from allauth.socialaccount.views import signup

urlpatterns = [
    path("signup/", signup, name="signup"),
    path('',home,name="home"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
]
