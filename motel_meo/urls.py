from django.urls import path
from .views import home , book_room_page, book_room, my_booking, edit_booking, delete_booking, contact, success_view,about_page, services_page, search
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", home, name="home-page"),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=False,template_name='account/login.html'), name='custom-login'),
    # path('login-redirect/', login_redirect, name='login-redirect'),
    # path('accounts/profile/', profile_view, name='profile'),
    path("search/", search, name="search-page"),
    path("book-room/", book_room_page, name="book-room-page"),
    path("book-room/book/",book_room,name="bookroom"),
    path("my-booking/",my_booking,name="my-booking"), 
    path('edit-booking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('delete-booking/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('contact/', contact, name='contact'),
    path('success/', success_view, name='success_url'),
    path("about/", about_page, name="about_page"),
    path("services/", services_page, name="services_page"),
]