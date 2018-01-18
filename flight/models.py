from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=500)

    class Meta:
        unique_together = ('firstname', 'lastname', 'dob')

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Employee(Person):
    salary = models.PositiveIntegerField()
    job = models.CharField(max_length=100)
    picture = models.FileField(default='anonymous.png')

    def name(self):
        return self.firstname + ' ' + self.lastname

    def get_absolute_url(self):
        return reverse('flight:employee-detail', kwargs={'pk': self.pk})


class AirCrew(Employee):
    total_flying_hours = models.PositiveIntegerField()


class Pilot(AirCrew):
    license_number = models.CharField(max_length=100, unique=True)


class Plane(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    manufacturer = models.CharField(max_length=50)
    aircraft_model = models.CharField(max_length=50)
    nb_rows_of_seats = models.PositiveSmallIntegerField()
    nb_col_of_seats = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.manufacturer + ' ' + self.aircraft_model + ' - ' + self.registration_number

    def get_absolute_url(self):
        return reverse('flight:other-index')


class Airport(models.Model):
    three_letters_code = models.CharField(max_length=3)
    name = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' (' + self.three_letters_code + ')'

    def get_absolute_url(self):
        return reverse('flight:other-index')


class Departure(models.Model):
    time = models.DateTimeField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    pilot_1 = models.ForeignKey(Pilot, related_name='pilot_1')
    pilot_2 = models.ForeignKey(Pilot, related_name='pilot_2')
    aircrew_1 = models.ForeignKey(AirCrew, related_name='aircrew_1')
    aircrew_2 = models.ForeignKey(AirCrew, related_name='aircrew_2')

    def __str__(self):
        return self.airport.name + ' - ' + str(self.time)

    def get_crew(self):
        return [self.pilot_1, self.pilot_2, self.aircrew_1, self.aircrew_2]

    def get_absolute_url(self):
        return reverse('flight:other-index')

    def save(self, *args, **kwargs):
        if self.pilot_1 == self.pilot_2 or self.aircrew_1 == self.aircrew_2:
            return reverse('flight:index')
        else:
            return super(Departure, self).save(*args, **kwargs)


class Arrival(models.Model):
    time = models.DateTimeField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

    def __str__(self):
        return self.airport.name + ' - ' + str(self.time)

    def get_absolute_url(self):
        return reverse('flight:other-index')


class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure = models.OneToOneField(Departure, on_delete=models.CASCADE)
    arrival = models.OneToOneField(Arrival, on_delete=models.CASCADE)

    def total_seats_nb(self):
        return self.plane.nb_col_of_seats * self.plane.nb_rows_of_seats - self.booking_set.count()

    def get_absolute_url(self):
        return reverse('flight:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.flight_number


class Booking(models.Model):
    booking_number = models.CharField(max_length=50, unique=True)
    price = models.FloatField(default=100)
    flight = models.ForeignKey(Flight)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_number


class Customer(Person):
    booking = models.ForeignKey(Booking)
