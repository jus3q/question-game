from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse(f"ID {question_id}")