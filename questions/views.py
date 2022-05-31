from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
import random
from django.forms import ModelForm
from questions.models import Rating
# from .forms import RateForm, AdvertisePostForm
from django import forms
import numpy as np
from django.contrib.auth import get_user_model
User = get_user_model()


def index(request):
    '''
    get length of questins in database
    randomly choose 3
    output those 3
    '''
    length_questions = count=len(Question.objects.all())
    q_list = [Question.objects.all()[random.randint(0,length_questions-1)] for x in range(3) ]
    context = {'q_list': q_list}
    return render(request, 'questions/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    all_ratings = Rating.objects.filter(question_id=question_id)
    rating_list = ([all_ratings[x].rating_recieved for x in range(len(all_ratings))])
    avg_rating = round(np.mean(rating_list),2)

    your_ratings = Rating.objects.filter(question_id=question_id)

    # print(avg_rating)

    return render(request, 'questions/detail.html', {'question': question, 'avg_rating':avg_rating})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    rating = request.POST['vote_result']
    print(question, rating)
    obj = Rating(question=question, rating_recieved=rating,user=request.user )
    obj.save()


 
    # try:
    #     rating = request.POST['vote_result']
    #     print(f'rating {rating}')
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'questions/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # try:
    #     rating = request.POST['vote_result']
        
    #     # selected_choice = question.rating_set.get(pk=rating)
    #     print('selected_choice')
    #     print(selected_choice)
    # except: 
    #     pass
    # print(f"the questions is {question}")

    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return HttpResponseRedirect(reverse('questions:index'))