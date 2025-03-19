print("Loading forms.py")
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        print("feedback form")
        fields = ['name', 'email', 'message','type','rating']