from django.contrib import admin

# Register your models here.
from .models import QuestionQuiz, AnswerQuiz

admin.site.register(QuestionQuiz)
admin.site.register(AnswerQuiz)