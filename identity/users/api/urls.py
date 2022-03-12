from django.urls import path
from .views import UsersList, UserDetails, UserFromToken

app_name = 'users-api'

urlpatterns = [
    # user
    path("", UsersList.as_view(), name="list"),
    path("<int:pk>/", UserDetails.as_view(), name="details"),
    path("me/", UserFromToken.as_view(), name="me"),
]
