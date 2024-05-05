from django.urls import path
from .views import home, book_room_page,book_room, my_booking,edit_booking, delete_booking
urlpatterns = [
    path("", home, name="home-page"),
    path("book-room/", book_room_page, name="book-room-page"),
    path("book-room/book/",book_room,name="bookroom"),
    path("my-booking/",my_booking,name="my-booking"),   
    path('edit-booking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('delete-booking/<int:booking_id>/', delete_booking, name='delete_booking'),
]