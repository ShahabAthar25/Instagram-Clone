from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import *

router = DefaultRouter()
router.register('', TweetViewSet, basename="tweets")

reply_router = NestedDefaultRouter(router, '', lookup="tweet_reply")
reply_router.register('replies', ReplyViewset, basename='replies')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(reply_router.urls)),
]

