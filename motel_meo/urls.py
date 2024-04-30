from django.urls import path
from .views import home, sign_up, log_in, book_room_page,log_out,book_room

urlpatterns = [
    path("", home, name="home-page"),
    path("signup/", sign_up,name="sign-up"),
    path("login/", log_in,name="log-in"),
    path("logout/",log_out,name="log-out"),
    path("book-room/", book_room_page, name="book-room-page"),
    path("book-room/book/",book_room,name="bookroom")
   
]

