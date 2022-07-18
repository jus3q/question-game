from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
import random
from django.forms import ModelForm
from questions.models import Rating, Question
# from .forms import RateForm, AdvertisePostForm
from django import forms
import numpy as np
import csv
from django.contrib.auth import get_user_model

User = get_user_model()





def index(request):
    '''
    add options to filter by rating, user, ...
    '''
    length_questions = count=len(Question.objects.all())
    q_list = [Question.objects.all()[random.randint(0,length_questions-1)] for x in range(3) ]
    context = {'q_list': q_list}
    return render(request, 'questions/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # Get All Ratings
    all_ratings = Rating.objects.filter(question_id=question_id)
    rating_list = ([all_ratings[x].rating_recieved for x in range(len(all_ratings))])
    avg_rating = round(np.mean(rating_list),2)
    # Get Your Rating -if your logged in
    try:
        your_ratings = Rating.objects.filter(question_id=question_id, user=request.user)
        your_rating_list = ([your_ratings[x].rating_recieved for x in range(len(your_ratings))])
        your_avg_rating = round(np.mean(your_rating_list),2)
    except:
        your_avg_rating = None
    # Get Guest Rating    
    guest_ratings = Rating.objects.filter(question_id=question_id, user=None)
    guest_rating_list = ([guest_ratings[x].rating_recieved for x in range(len(guest_ratings))])
    guest_avg_rating = round(np.mean(guest_rating_list),2)

    return render(request, 'questions/detail.html', {'question': question, 
                                                    'avg_rating':avg_rating,
                                                    'your_avg_rating':your_avg_rating,
                                                    'guest_avg_rating':guest_avg_rating,
                                                     })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    rating = request.POST['vote_result']
    print(question, rating)
    try:
        obj = Rating(question=question, rating_recieved=rating, user=request.user )
    except:
        obj = Rating(question=question, rating_recieved=rating, )
    finally:
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



def build_data(request):
    add_list = []
    did_not_add_list = []
    with open("sample.txt", "r") as fp:
        for row in csv.reader(fp, delimiter=':'):
            print(row)
            is_question = Question.objects.filter(question_text=row[0])
            print(is_question)

            if is_question.exists():
                # print("it exists")
                did_not_add_list.append(row[0])
            else:
                add_list.append(row[0])
                try:
                    obj = Question(question_text=row[0], title=row[1], )
                except:
                    obj = Question(question_text=row[0], )
                obj.save()
    response_text = f'added {add_list} | did not add {did_not_add_list}'
    return HttpResponse(response_text)