from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import SocialAccountListView
from .views import GithubLogin, GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    # dj-rest-auth
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("dj-rest-auth/github/", GithubLogin.as_view(), name="github"),
    path("dj-rest-auth/google/", GoogleLogin.as_view(), name="google"),
    path("social-accounts/", SocialAccountListView.as_view(), name="social_account_list"),

]
