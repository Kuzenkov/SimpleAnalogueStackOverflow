from django.forms import ModelForm
from questions.models import Answer


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
