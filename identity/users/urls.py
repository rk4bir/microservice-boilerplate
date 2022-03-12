from django.urls import path
from .views import (
    SignInView,
    sign_out,
    SignUpView,
    PasswordRecoveryView,
    ProfileHome,
    ChangePassword,
    PasswordRecoveryCodeCheckView
)

from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path("", login_required(ProfileHome.as_view()), name='home'),
    path("sign-in/", SignInView.as_view(), name='sign-in'),
    path("sign-up/", SignUpView.as_view(), name='sign-up'),
    path("sign-out/", sign_out, name='sign-out'),
    path("change-password/", login_required(ChangePassword.as_view()), name='change-password'),
    path("password-recovery/", PasswordRecoveryView.as_view(), name='password-recovery'),
    path("reset-password/<str:key>/", PasswordRecoveryCodeCheckView.as_view(), name='reset-code-check'),
]
