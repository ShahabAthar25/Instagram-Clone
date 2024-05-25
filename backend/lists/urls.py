from django.urls import path
from .views import *

urlpatterns = [
    path("", ListCreateListsView.as_view(), name="list-create-lists"),
    path("<int:pk>/", RetrieveUpdateDestroy.as_view(), name="retrieve-update-destroy-lists"),
    path("<int:pk>/following", FollowingListUsersView.as_view(), name="following-users-lists"),
    path("<int:pk>/followed", FollowingListUsersView.as_view(), name="followed-users-lists"),
    path("<int:pk>/follow", FollowUnfollowListView.as_view(), name="follow-users-lists"),
]
