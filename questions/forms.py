from django.forms import ModelForm, Textarea
from questions.models import Answer, Question


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
        widgets = {
            'answer_text': Textarea(attrs={'cols': 70, 'rows': 10}),
        }


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'question']

    def __init__(self, *args, **kwargs):
        self.owner = kwargs['initial']['owner']
        super(QuestionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(QuestionForm, self).save(False)
        obj.owner = self.owner
        commit and obj.save()
        return obj
