from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import View
from .models import Flight, Employee
from .forms import UserForm


#---------Flights---------
class IndexView(generic.ListView):
    template_name = 'flight/index.html'
    context_object_name = 'all_flights'

    def get_queryset(self):
        return Flight.objects.all()

@method_decorator(login_required, name='dispatch')
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
@method_decorator(login_required, name='dispatch')
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


#---------Users---------
class UserFormView(View):
    form_class = UserForm
    template_name = 'flight/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #Normalized data (formated properly)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #Check if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('flight:index')

        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'flight/index.html')
            else:
                return render(request, 'flight/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'flight/login.html', {'error_message': 'Invalid login'})
    return render(request, 'flight/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'flight/login.html', context)