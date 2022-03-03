import datetime
import uuid

from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    username = models.CharField(max_length=200)
    password = models.CharField
    USER_TYPE = [(0, "Student"), (1, "Staff")]
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE,
    )
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


# class Course(models.Model):
#     course_id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False)
#     course_name = models.CharField(max_length=200)
#     num_of_std = models.IntegerField()
#
#     def __str__(self):
#         return self.course_name


class Submission(models.Model):
    submission_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


datetime.timedelta(days=1)


class Comment(models.Model):
    comment_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    comment_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.
