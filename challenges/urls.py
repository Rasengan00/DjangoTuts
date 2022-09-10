from django.urls import path
from . import views

appName = "challenges"

urlpatterns = [
    path("<int:week>",views.index_by_number,name="weekChalengeNumber"),
    path("",views.index,name="weekChalenge")
]