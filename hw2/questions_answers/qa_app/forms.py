from django import forms
from .models import Question, Answer

class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('topic', 'text')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('question', 'text')
