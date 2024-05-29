from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import SocialAccountListView
from .views import GithubLogin, GoogleLogin, send_welcome_email, FacebookLogin
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView,TokenVerifyView
urlpatterns = [
    path('admin/', admin.site.urls),
    # dj-rest-auth
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("dj-rest-auth/github/login/", GithubLogin.as_view(), name="github"),
    path("dj-rest-auth/google/login/", GoogleLogin.as_view(), name="google"),
    path("social-accounts/", SocialAccountListView.as_view(), name="social_account_list"),
    path("send-welcome-email/", send_welcome_email, name="send-welcome-email"),
    path("dj-rest-auth/facebook/login/", FacebookLogin.as_view(), name="facebook"),
    path("dj-rest-auth/token/", TokenObtainPairView.as_view()),
    path("dj-rest-auth/token/refresh/", TokenRefreshView.as_view()),
    path("dj-rest-auth/token/verify/", TokenVerifyView.as_view())

]
