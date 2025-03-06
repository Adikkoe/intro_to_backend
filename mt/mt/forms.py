from django import forms
from .models import Table, Reservation

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'seats', 'status']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'table', 'date', 'time', 'status']
