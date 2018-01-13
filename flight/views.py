from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Flight, Employee


#---------Flights---------
class IndexView(generic.ListView):
    template_name = 'flight/index.html'
    context_object_name = 'all_flights'

    def get_queryset(self):
        return Flight.objects.all()


class DetailView(generic.DetailView):
    model = Flight
    template_name = 'flight/detail.html'


class FlightCreate(CreateView):
    model = Flight
    fields = ['flight_number', 'plane', 'departure', 'arrival']


class FlightUpdate(UpdateView):
    model = Flight
    fields = ['flight_number', 'plane', 'departure', 'arrival']


class FlightDelete(DeleteView):
    model = Flight
    success_url = reverse_lazy('flight:index')

#---------Employees---------

class EmployeesIndexView(generic.ListView):
    template_name = 'flight/employees.html'
    context_object_name = 'all_employees'

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeDetailView(generic.DetailView):
    model = Employee
    template_name = 'flight/employee_detail.html'


class EmployeeCreate(CreateView):
    model = Employee
    fields = ['firstname', 'lastname', 'dob', 'address', 'job', 'salary', 'picture']


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['firstname', 'lastname', 'dob', 'address', 'job', 'salary', 'picture']


class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('flight:employee-index')