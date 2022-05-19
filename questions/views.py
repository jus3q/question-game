from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
import random


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
    return render(request, 'questions/detail.html', {'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))