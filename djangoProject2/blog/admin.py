from django.contrib import admin

from .forms import CreateSubmissionForm
from .models import Question, Choice, Submission, User


# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub-date', 'question_text']


class SubmissionAdmin(admin.ModelAdmin):
    add_form = CreateSubmissionForm
    model = Submission
    list_display = ['id', 'title', 'pub_date', 'content']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(User)
