from django.contrib import admin
from .models import Question, Choice, Submission, User


# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub-date', 'question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(User)