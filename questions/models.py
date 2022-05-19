import datetime
from re import T

from django.db import models
from django.utils import timezone
from django.conf import settings


class Question(models.Model):
    title = models.CharField(max_length=100)
    question_text = models.TextField(blank=False, null=True)
    pub_date = models.DateTimeField('date published')
    timestamp = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Rating(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    rate_number = models.IntegerField(default=5)

