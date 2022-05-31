from django.contrib import admin

from .models import Question, Rating

admin.site.register(Question)
admin.site.register(Rating)
