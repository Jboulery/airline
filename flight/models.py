from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=500)

class Employee(Person):
    salary = models.PositiveIntegerField()
    job = models.CharField(max_length=100)

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

class Airport(models.Model):
    three_letters_code = models.CharField(max_length=3) #Regex Validator needed
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Departure(models.Model):
    time = models.DateTimeField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    pilot_1 = models.ForeignKey(Pilot, related_name='pilot_1')
    pilot_2 = models.ForeignKey(Pilot, related_name='pilot_2')
    aircrew_1 = models.ForeignKey(AirCrew, related_name='aircrew_1')
    aircrew_2 = models.ForeignKey(AirCrew, related_name='aircrew_2')

class Arrival(models.Model):
    time = models.DateTimeField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    departure = models.ForeignKey(Departure, on_delete=models.CASCADE)
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE)

class Booking(models.Model):
    booking_number = models.CharField(max_length=50)
    price = models.FloatField()
    flight = models.ForeignKey(Flight)

class Customer(Person):
    booking = models.ForeignKey(Booking)
