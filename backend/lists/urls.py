from django.urls import path
from .views import *

urlpatterns = [
    path("", ListCreateListsView.as_view(), name="list-create-lists"),
    path("<int:pk>/", RetrieveUpdateDestroy.as_view(), name="retrieve-update-destroy-lists"),
]
