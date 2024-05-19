from django import forms

from .models import *

class TweetCeationChangeForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ('content', 'quote_tweet')

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image', 'description')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'allow_multiple_selected': True}),
        }