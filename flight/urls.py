from django.conf.urls import url
from . import views

app_name = 'flight'

urlpatterns = [
    #/flight
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/flight/<flight_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
]
