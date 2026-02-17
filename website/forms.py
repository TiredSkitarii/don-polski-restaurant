from django import forms
from restaurant_booking.models import Booking_Info
from datetime import datetime, timedelta, time

# generates times for the booking form. originally written by Bear81


def generate_time_choices(start=time(12, 0), end=time(22, 0), interval=30):
    current = datetime.combine(datetime.today(), start)
    end_dt = datetime.combine(datetime.today(), end)
    choices = []
    while current <= end_dt:
        t = current.time()
        choices.append((t.strftime("%H:%M"), t.strftime("%H:%M")))
        current += timedelta(minutes=interval)
    return choices


class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.DateInput(attr={'type': 'date', 'class': 'form-control'})
    )
    booking_time = forms.ChoiceField(
        choices=generate_time_choices(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    number_of_guests = forms.IntegerField(min_value=1)
