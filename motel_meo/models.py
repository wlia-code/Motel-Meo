from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Hotel(models.Model):
    """
    Represents a hotel with basic information.
    """
    name = models.CharField(max_length=45, default="Motel-Meo")
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = "Hotels"

class Room(models.Model):
    """
    Represents a room within a hotel.
    """
    ROOM_TYPE = (
        ("1", "Single"),
        ("2", "Double"),
        ("3", "Suite"),
        ("4", "Triple")
    )

    ROOM_STATUS = (
        ("1", "Available"),
        ("2", "Not Available")
    )

    room_type = models.CharField(max_length=50, choices=ROOM_TYPE)
    status = models.CharField(max_length=50, choices=ROOM_STATUS)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    capacity = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    room_no = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'http://bulma.io/images/placeholders/1280x960.png'

    def __str__(self):
        return f"Hotel: {self.hotel.name} -- Room: {self.room_type} -- Price: {self.price}"

    class Meta:
        verbose_name_plural = "Rooms"

class Booking(models.Model):
    """
    Represents a booking made by a customer.
    """
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=155, default="null")
    person = models.IntegerField(default=1)  

    def __str__(self):
        return f"Customer: {self.customer.username} -- Booking ID: {self.booking_id}"

    class Meta:
        verbose_name_plural = "Booking"
