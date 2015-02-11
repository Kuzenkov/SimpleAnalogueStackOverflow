from django.contrib import admin
from questions.models import Question, Answer


class QuestionInline(admin.StackedInline):
    """Class for adding comments to question."""
    model = Answer
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Class for administration Question objects."""
    inlines = [QuestionInline]
    list_filter = ['created_on']
