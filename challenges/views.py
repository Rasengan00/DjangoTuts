import imp
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

weekly_challenge = {
    "Mon":"Mon challenge",
    "Tue":"Tue challenge",
    "Web":"Web challenge",
    "Thu":"Thu challenge",
    "Fri":"Fri challenge"
}

# Create your views here.
def index_by_number(request,week):
    weeks = list(weekly_challenge.keys())

    if week > len(weeks):
        return HttpResponseNotFound("invalid week")

    redirect_week = weeks[week-1]
    redirect_url = reverse('weekChalenge',args=[redirect_week])
    return HttpResponseRedirect(redirect_url)

def index(request):
    context = {"message":"yo boy it's your keshav"}
    try:
        return render(request,"challenges/index.html",context)
    except:
        return HttpResponseNotFound("This week day not supported")
