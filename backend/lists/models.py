from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

from tweets.models import Tweet

User = get_user_model()

class List(models.Model):
    users = models.ManyToManyField(User, related_name="users_set", blank=True)
    tweets = models.ManyToManyField(Tweet, related_name="tweets_set", blank=True)
    title = models.CharField(max_length=255, validators=[MinLengthValidator(10)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"