from django.urls import path
from .views import *

urlpatterns=[
   #path("liste/",views.all_conference,name='all_conference')
   path("liste/",ConferenceList.as_view(),name='all_conference'),
   path("conference/<int:pk>/",ConferenceDetails.as_view(),name='conference-details'),
   path("form/",ConferenceCreate.as_view(),name='conference-add'),
   path("<int:pk>/edit",ConferenceUpdate.as_view(),name='conference-edit'),
   path("<int:pk>/delete",ConferenceDelete.as_view(),name='conference-delete')


]