from django.urls import path
from . import views
from main.views import signupView

# app urls
appname = "main"
urlpatterns = [
    # main urls
    path("", views.index, name="index"),
    path("articles/", views.articles, name="articles"),
    path("articles/privacy policy", views.privacy_policy, name="privacy"),
    path("articles/cookies policy", views.cookies_policy, name="cookies"),
    path("energy usage/", views.energyUsage, name="energyusage"),
    # user creation and profile based urls
    path("accounts/signup/", signupView.as_view(), name="signup"),
    path("accounts/profile/", views.profile, name="profile"),
    path("accounts/profile/appointment/", views.appointment, name="appointment"),
    path("accounts/profile/payment/", views.payment, name="payment"),
    path(
        "accounts/profile/carbon footprint/", views.carbonFootprint, name="carbonfoot"
    ),
]
