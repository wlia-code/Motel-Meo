from django.test import TestCase, Client
from django.urls import reverse
from .models import Hotel, Room, Booking
from django.contrib.auth.models import User
from datetime import date, timedelta

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # Define URLs
        self.home_url = reverse('home-page')
        self.book_room_url = reverse('book-room-page')
        self.book_room_confirm_url = reverse('bookroom')
        self.my_booking_url = reverse('my-booking')
        self.edit_booking_url = reverse('edit_booking', args=[1])
        self.delete_booking_url = reverse('delete_booking', args=[1])

        # Create test objects
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.hotel = Hotel.objects.create(name="Hotel A", location="Location A", state="State A")
        self.room = Room.objects.create(room_type="Single", status="Available", price=100, capacity=1, size=20, room_no=101, hotel=self.hotel)
        self.booking = Booking.objects.create(check_in=date.today(), check_out=date.today() + timedelta(days=1), room=self.room, customer=self.user, booking_id="123")

    def test_home_view(self):
        """Test home page view"""
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_book_room_page_view(self):
        """Test book room page view"""
        response = self.client.get(self.book_room_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookroom.html')

    def test_book_room_view(self):
        """Test booking a room view"""
        response = self.client.post(self.book_room_confirm_url, {
            'room_id': self.room.id,
            'check_in': date.today() + timedelta(days=2),
            'check_out': date.today() + timedelta(days=3),
            'person': 1
        })
        self.assertEquals(response.status_code, 302)  # Redirects after successful booking

    def test_my_booking_view(self):
        """Test my booking view"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.my_booking_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_booking.html')

    def test_edit_booking_view(self):
        """Test edit booking view"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.edit_booking_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html')

    def test_delete_booking_view(self):
        """Test delete booking view"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.delete_booking_url)
        self.assertEqual(response.status_code, 302)  
