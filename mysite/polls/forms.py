from django import forms
from . import models

class CreateQuestion(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['question_label', 'question_text']
