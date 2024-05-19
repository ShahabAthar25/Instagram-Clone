from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

User = get_user_model()

class Tweet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    quote_tweet = models.ForeignKey('self', on_delete=models.SET_NULL, related_name="quoted_by", blank=True, null=True)
    
    def __str__(self):
        return f"@{self.owner.username}'s Tweet (ID: {self.pk})"

class Image(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="tweets/")
    description = models.CharField(max_length=280, blank=True, null=True)
    
    def __str__(self):
        return f"Image for tweet (ID: {self.tweet.pk})"