from django.urls import path
from .views import RegisterView , GoogleLogin


from allauth.socialaccount.views import signup

urlpatterns = [
    path("signup/", signup, name="socialaccount_signup"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
