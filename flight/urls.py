from django.conf.urls import url
from . import views

app_name = 'flight'

urlpatterns = [
    #/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/flight/<flight_id>/
    url(r'^flight/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/flight/add
    url(r'^flight/add/$', views.FlightCreate.as_view(), name='flight-add'),

    #/flight/<flight_id>/update/
    url(r'^flight/(?P<pk>[0-9]+)/update/$', views.FlightUpdate.as_view(), name='flight-update'),

    #/flight/<flight_id>/delete/
    url(r'^flight/(?P<pk>[0-9]+)/delete/$', views.FlightDelete.as_view(), name='flight-delete'),
]
