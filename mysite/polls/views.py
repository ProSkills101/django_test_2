from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Vote

# Create your views here.

def mypolls(request):
  if request.user.is_authenticated:
    questions = Question.objects.filter(user=request.user).order_by('-created')
    context = {'questions': questions}
    return render(request, 'polls/mypolls.html', context)

  return HttpResponse('Unauthorized', status=401)

def mypolls_create(request):
  if request.user.is_authenticated:
    if request.method == 'GET':
      return render(request, 'polls/mypolls-create.html')
    elif request.method == 'POST':
      qtext = request.POST.get('question-text')
      if not qtext:
        return HttpResponse("Question does not exist", status=404)
      
      question = Question(user=request.user, question_text=qtext, state='closed')
      question.save()
      
      return HttpResponseRedirect(reverse('polls:mypolls'))

  return HttpResponse('Unauthorized', status=401)

def mypolls_update(request, question_id):
  if request.user.is_authenticated:
    question = Question.objects.get(pk=question_id)
    choices = question.choice_set.all()

    if not question:
      return HttpResponse("Question does not exist", status=404)

    if request.method == 'GET':
      context = {'question': question, 'choices': choices}
      return render(request, 'polls/mypolls-update.html', context)
      
    elif request.method == 'POST':
      qtext = request.POST.get('question-text')
      if not qtext:
        return HttpResponse("Question does not exist", status=404)
      question.question_text = qtext
      question.save()
 
      for key in request.POST:
        if key.startswith('choice-text'):
          text = request.POST.get(key)
          if not text:
            return HttpResponse("Question does not exist", status=404)
          tokens = key.split('-')
          cid = tokens[2]
          for choice in choices:
            if str(choice.id) == cid:
              choice.choice_text = text
              choice.save()
          
      ctext = request.POST.get('choice-new')
      if ctext:
        choice = Choice(user=request.user, question=question, choice_text=ctext)
        choice.save()

      return HttpResponseRedirect(reverse('polls:mypolls'))
  
  return HttpResponse('Unauthorized', status=401)

def mypolls_delete(request, question_id):
  if request.user.is_authenticated:
    if request.method == 'DELETE':
      question = Question.objects.get(pk=question_id)

      if not question:
        return JsonResponse({ 'status': '404', 'msg': 'not found'})
      
      question.delete()
      return JsonResponse({ 'status': '200', 'msg': 'success'})
  
  return JsonResponse({ 'status': '401', 'msg': 'unauthorized'})

def mypolls_delete_choice(request, question_id, choice_id):
  if request.user.is_authenticated:
    if request.method == 'DELETE':
      question = Question.objects.get(pk=question_id)

      if not question:
        return JsonResponse({ 'status': '404', 'msg': 'not found'})

      choices = question.choice_set.all()
      for choice in choices:
        if choice.id == choice_id:
          choice.delete()
      
      return JsonResponse({ 'status': '200', 'msg': 'success'})
  
  return JsonResponse({ 'status': '401', 'msg': 'unauthorized'})

def index(request):
  latest_question_list = Question.objects.filter(state='open').order_by('-created')
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  if request.user.is_authenticated:
    try:
      question = Question.objects.get(pk=question_id)
      if question.state != 'open':
        raise Http404("Question does not exist")  
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question })
  else:
    return HttpResponse('Unauthorized', status=401)

def result(request, question_id):
    try:
      question = Question.objects.get(pk=question_id)
      if question.state != 'open':
        raise Http404("Question does not exist")
        
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/result.html', {'question': question })

def vote(request, question_id):
  if request.user.is_authenticated:
    try:
      question = Question.objects.get(pk=question_id)
      if question.state != 'open':
        raise Http404("Question does not exist")

      selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #selected_choice.votes += 1
        vote = Vote(question=question, choice=selected_choice, user=request.user)
        vote.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
  else:
    return HttpResponse('Unauthorized', status=401)