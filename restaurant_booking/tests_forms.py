from django.test import TestCase
from django.contrib.auth.models import User
from restaurant_booking.models import Table
from website.forms import BookingForm

# Create your tests here.

class TestBookingForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.table = Table.objects.create(table_number='A1', capacity=4)

    def test_form_missing_required_fields(self):
        form = BookingForm(data={
            'user': self.user,
            'booking_date': '02/23/2026',
            'booking_time': '16:00',
            'number_of_guests': 3
        })
        self.assertTrue(form.is_valid(), f"Form should be valid but has the following errors: {form.errors}") 
