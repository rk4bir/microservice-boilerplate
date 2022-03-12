from django.urls import path
from .views.application import (
    ApplicationRegistration,
    ApplicationList,
    ApplicationDetail,
    ApplicationUpdate,
    ApplicationDelete,
)
from oauth2_provider import views

app_name = 'oauth2'

urlpatterns = [
    # app authorization
    path("authorize/", views.AuthorizationView.as_view(), name="authorize"),
    path("token/", views.TokenView.as_view(), name="token"),
    path("revoke_token/", views.RevokeTokenView.as_view(), name="revoke-token"),
    path("introspect/", views.IntrospectTokenView.as_view(), name="introspect"),
    # token management
    path("authorized_tokens/", views.AuthorizedTokensListView.as_view(),
         name="authorized-token-list"),
    path("authorized_tokens/<int:pk>/delete/",
         views.AuthorizedTokenDeleteView.as_view(), name="authorized-token-delete"),
    # app crud
    path("apps/", ApplicationList.as_view(), name="apps"),
    path("apps/register/", ApplicationRegistration.as_view(), name="apps-register"),
    path("apps/<int:pk>/", ApplicationDetail.as_view(), name="apps-detail"),
    path("apps/<int:pk>/delete/", ApplicationDelete.as_view(), name="apps-delete"),
    path("apps/<int:pk>/update/", ApplicationUpdate.as_view(), name="apps-update"),
]
