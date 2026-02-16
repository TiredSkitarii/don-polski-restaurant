from django.shortcuts import render, redirect
from .models import Booking_Info, Table
from website.forms import BookingForm
from django.contrib import messages

# Create your views here.


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.booking_date = form.booking_date
            booking.booking_time = form.booking_time
            booking.user = request.user
            booking.save()
            messages.success(request, "Booking successfully created!")
            return redirect('home')
        else:
            messages.error(request, "there was a problem with your booking.")
    else:
        form = BookingForm()
    return render(request, 'restaurant_booking/booking_form.html', {'form': form, 'booking': None})
