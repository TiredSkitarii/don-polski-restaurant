from django import forms
from restaurant_booking.models import Booking_Info
from django.utils import timezone
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
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    booking_time = forms.ChoiceField(
        choices=generate_time_choices(),
        widget=forms.Select(attrs={'type': 'time', 'class': 'form-control'})
    )

    class Meta:
        model = Booking_Info
        fields = ['user', 'number_of_guests']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        initial = kwargs.get('initial', {})

        if instance and instance.booking_datetime:
            initial['booking_date'] = instance.booking_datetime.date()
            initial['booking_time'] = instance.booking_datetime.time().strftime('%H:%M')
            kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        if booking_date and booking_time:
            try:
                booking_datetime = datetime.strptime(
                    f"{booking_date} {booking_time}", "%y-%m-%d %H:%M"
                )

                if timezone.is_naive(booking_datetime):
                    booking_datetime = timezone.make_aware(
                         booking_datetime, timezone.get_current_timezone()
                    )

                if booking_datetime < timezone.now():
                    self.add_error('booking-date', "Booking must be for a future date!")

                cleaned_data['booking_datetime'] = booking_datetime

            except ValueError:
                self.add_error('booking_time', "Invalid time format")

        return cleaned_data
