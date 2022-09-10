import imp
from multiprocessing import context
from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

weekly_challenge = {
    "Mon":"Mon challenge",
    "Tue":"Tue challenge",
    "Web":"Web challenge",
    "Thu":"Thu challenge",
    "Fri":None
}

# Create your views here.
def index(request):
    keys = list(weekly_challenge.keys())
    context ={"weeks":keys}
    try:
        return render(request,"challenges/index.html",context)
    except:
        raise Http404()

def weekchallenge(request,week):
    try:
        context={
        "week":week,
        "challenge":weekly_challenge[week]
        }
        return render(request,"challenges/challenge.html",context)
    except:
        raise Http404()

def week_challenge_by_number(request,week):
    weeks = list(weekly_challenge.keys())

    if week > len(weeks):
        raise Http404

    redirect_week = weeks[week-1]
    redirect_url = reverse('weekChalenge',args=[redirect_week])
    return HttpResponseRedirect(redirect_url)

