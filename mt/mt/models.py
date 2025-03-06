from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('reserved', 'Reserved')])

    def __str__(self):
        return f'Үстел {self.number}'

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')])

    def __str__(self):
        return f'{self.user.name} - {self.table.number} ({self.date})'
