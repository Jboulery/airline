from django.db import models
from django.core.urlresolvers import reverse


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Employee(Person):
    salary = models.PositiveIntegerField()
    job = models.CharField(max_length=100)
    picture = models.FileField(default='anonymous.png')

    def get_absolute_url(self):
        return reverse('flight:employee-detail', kwargs={'pk': self.pk})


class AirCrew(Employee):
    total_flying_hours = models.PositiveIntegerField()


class Pilot(AirCrew):
    license_number = models.CharField(max_length=100)


class Plane(models.Model):
    registration_number = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50)
    aircraft_model = models.CharField(max_length=50)
    nb_rows_of_seats = models.PositiveSmallIntegerField()
    nb_col_of_seats = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.manufacturer + ' ' + self.aircraft_model + ' - ' + self.registration_number


class Airport(models.Model):
    # Regex Validator needed
    three_letters_code = models.CharField(max_length=3)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' (' + self.three_letters_code + ')'


class Departure(models.Model):
    time = models.DateTimeField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    pilot_1 = models.ForeignKey(Pilot, related_name='pilot_1')
    pilot_2 = models.ForeignKey(Pilot, related_name='pilot_2')
    aircrew_1 = models.ForeignKey(AirCrew, related_name='aircrew_1')
    aircrew_2 = models.ForeignKey(AirCrew, related_name='aircrew_2')

    def __str__(self):
        return self.airport.name + ' - ' + str(self.time)


class Arrival(models.Model):
    time = models.DateTimeField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    def __str__(self):
        return self.airport.name + ' - ' + str(self.time)


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure = models.ForeignKey(Departure, on_delete=models.CASCADE)
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE)

    def total_seats_nb(self):
        return self.plane.nb_col_of_seats * self.plane.nb_rows_of_seats - self.booking_set.count()

    def get_absolute_url(self):
        return reverse('flight:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.flight_number


class Booking(models.Model):
    from datetime import datetime
    booking_number = models.CharField(max_length=50)
    price = models.FloatField(default=100)
    flight = models.ForeignKey(Flight)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_number


class Customer(Person):
    booking = models.ForeignKey(Booking)
