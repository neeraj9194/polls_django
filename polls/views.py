from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question
from django.template import RequestContext,loader
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    latest_ques=Question.objects.order_by('-pub_date')[:5]
    #template=loader.get_template('polls/index.html')
    context=RequestContext(request,{'latest_ques':latest_ques,})
    #output=', 'join([p.ques_text for p in latest_ques])
    return render(request,'polls/index.html',context)

def details(request,ques_id):
    question=get_object_or_404(Question,pk=ques_id)
    return render(request,'polls/details.html',{'question':question})
    #return HttpResponse("hello you are at  question  %s" %ques_id)

def vote(request,ques_id):
    p=get_object_or_404(Question,pk=ques_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST['choice'])
    except:
        return render(requesst,'polls/details.html',{'question':p,'error_message':"you did't select a choice",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result',args=(p.id,)))

def result(request,ques_id):
    q=get_object_or_404(Question,pk=ques_id)
    return render(request,'polls/result.html',{'question':q})
    #return HttpResponse("hello you are at results of question  %s" %ques_id)
