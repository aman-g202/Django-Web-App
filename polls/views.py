from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import Question, Choice

# from django.template import loader # to include template facility

def index(request):
	latest_question = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question' : latest_question}
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/details.html', {'question': question})	
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")

	return render(request, 'polls/results.html', {'question': question})	


    # response = "You're looking at the results of question %s."
    

def vote(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")

	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/details.html', {'error_message':'you didn\'t select a choice', 'question': question})

	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# Create your views here.
