print("Loading forms.py")
from django import forms
from .models import Feedback
from django import forms

from django.core.validators import MinValueValidator, MaxValueValidator

class FeedbackForm(forms.ModelForm):
    rating = forms.IntegerField(
        widget=forms.HiddenInput(),  # Use HiddenInput to manage the field via JavaScript
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        model = Feedback
        print("feedback form")
        
        fields = ['name', 'email', 'message','feedback_type','rating']
        labels = {
            'feedback_type': 'Feedback Type',
            #  'rating':'Rate our Service'
        }