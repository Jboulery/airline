from django.conf.urls import url
from . import views

app_name = 'flight'

urlpatterns = [
    #-------Flights-------
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

    #/search/
    url(r'^search/$', views.search_flights, name='flight-search'),

    #-------Employees-------
    #/employees
    url(r'^employees/$', views.EmployeesIndexView.as_view(), name='employee-index'),

    #/employees/search
    url(r'^employees/search/$', views.search_employees, name='employee-search'),

    #/employees/<employee_id>/
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeDetailView.as_view(), name='employee-detail'),

    #/employee/add
    url(r'^employee/add/$', views.EmployeeCreate.as_view(), name='employee-add'),

    #/employee/<employee_id>/update/
    url(r'^employee/(?P<pk>[0-9]+)/update/$', views.EmployeeUpdate.as_view(), name='employee-update'),

    #/employee/<employee_id>/delete/
    url(r'^employee/(?P<pk>[0-9]+)/delete/$', views.EmployeeDelete.as_view(), name='employee-delete'),

    #employee/<employee_id>/flights
    url(r'^employee/flights/$', views.employee_flights, name='employee-flights'),

    #-------Users-------
    #/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/login/
    url(r'^login/$', views.login_user, name='login'),

    #/logout/
    url(r'^logout/$', views.logout_user, name='logout'),

    # -------Bookings-------
    #/bookings/
    url(r'^bookings/$', views.BookingsView.as_view(), name='bookings'),

    #/bookings/confirmation/
    url(r'^bookings/confirmation/$', views.booking_confirmation, name='bookings-confirmation'),

    #/bookings/confirmed/
    url(r'^bookings/confirmed/$', views.booking_submitted, name='bookings-confirmed'),

    #-------Other-------
    #Other
    url(r'^other/$', views.other_index, name='other-index'),

    #/plane/add
    url(r'^plane/add/$', views.PlaneCreate.as_view(), name='plane-add'),

    #/airport/add
    url(r'^airport/add/$', views.AirportCreate.as_view(), name='airport-add'),

    # /Departure/add
    url(r'^departure/add/$', views.DepartureCreate.as_view(), name='departure-add'),

    # /Arrival/add
    url(r'^arrival/add/$', views.ArrivalCreate.as_view(), name='arrival-add'),

]
