from django.urls import path
from .views import *

urlpatterns=[
   #path("liste/",views.all_conference,name='all_conference')
   path("liste/",ConferenceList.as_view(),name='all_conference'),
   path("conference/<int:pk>/",ConferenceDetails.as_view(),name='conference-details')
]