from django.urls import path
from .views import Create, Retrieve, Update, Delete, List

app_name = "products-api"

urlpatterns = [
    path("", List.as_view(), name="list"),
    path("create/", Create.as_view(), name="create"),
    path("<slug:slug>/", Retrieve.as_view(), name="retrieve"),
    path("<slug:slug>/update/", Update.as_view(), name="update"),
    path("<slug:slug>/delete/", Delete.as_view(), name="delete"),
]
