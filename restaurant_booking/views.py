from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking_Info, Table
from website.forms import BookingForm
from django.contrib import messages

# Create your views here.


@login_required
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


@login_required
def change_booking(request, pk):
    booking = get_object_or_404(Booking_Info, pk=pk, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking.booking_date = form.booking_date
            booking.booking_time = form.booking_time
            booking.number_of_guests = form.number_of_guests
            booking.status = 'pending'
            booking.save()
            messages.success(request, "Booking updated!")
            return redirect('booking_list')
        else:
            messages.error(request, "Errors detected, please correct to continue")
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'restaurant_booking/booking_form.html', {'form': form, 'booking': booking})


@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking_Info, pk=pk, user=request.user)
    booking.status = 'cancelled'
    booking.save()
    return redirect('booking_list')


@login_required
def booking_list(request):
    bookings = Booking_Info.objects.filter(user=request.user)
    return render(request, 'restaurant_booking/booking_list.html', {'bookings': bookings})
