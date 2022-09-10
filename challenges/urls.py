from django.urls import path
from . import views

appName = "challenges"

urlpatterns = [
    path("<int:week>",views.week_challenge_by_number,name="weekChalengeNumber"),
    path("<str:week>",views.weekchallenge,name="weekChalenge"),
    path("",views.index,name="index")
]