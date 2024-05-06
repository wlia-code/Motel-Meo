from django.shortcuts import render, redirect, get_object_or_404
from .models import Hotel, Room, Booking
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SearchForm, UserRegistrationForm,BookingForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import get_object_or_404
from .forms import ContactForm


def home(request):
    """
    View function for the home page.
    Renders the home page with a search form and available rooms.
    """
    all_locations = Hotel.objects.values_list('location', 'id').distinct().order_by('location')
    available_rooms = None
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            try:
                search_location = form.cleaned_data['search_location']
                check_in = form.cleaned_data['check_in']
                check_out = form.cleaned_data['check_out']
                capacity = form.cleaned_data['capacity']

                reserved_room_ids = Booking.objects.filter(
                    room__hotel=search_location,
                    check_in__lt=check_out,
                    check_out__gt=check_in
                ).values_list('room_id', flat=True)

                available_rooms = Room.objects.filter(
                    hotel=search_location,
                    capacity__gte=capacity
                ).exclude(id__in=reserved_room_ids)

                if not available_rooms:
                    messages.warning(request, "Sorry, no rooms are available during this time period.")
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
    else:
        form = SearchForm()

    context = {'all_locations': all_locations, 'form': form, 'available_rooms': available_rooms}
    return render(request, 'index.html', context)


@login_required
def book_room_page(request):
    """
    View function for booking a room.
    Requires the user to be logged in.
    Renders the book room page with details of the selected room.
    """
    room_id = request.GET.get('roomid')
    if room_id is None:
        return HttpResponse("Room ID is missing.")
    try:
        room = Room.objects.get(id=int(room_id))
        return render(request, 'bookroom.html', {'room': room})
    except Room.DoesNotExist:
        return HttpResponse("Room not found.")


@login_required
def book_room(request):
    """
    View function for processing room booking requests.
    Requires the user to be logged in.
    """
    if request.method =="POST":
        room_id = request.POST['room_id']
        room = Room.objects.all().get(id=room_id)
        for booking in Booking.objects.all().filter(room = room):
            if str(booking.check_in) < str(request.POST['check_in']) and str(booking.check_out) < str(request.POST['check_out']):
                pass
            elif str(booking.check_in) > str(request.POST['check_in']) and str(booking.check_out) > str(request.POST['check_out']):
                pass
            else:
                messages.warning(request,"Sorry This Room is unavailable for Booking")
                return redirect("book_room_page")
            
        current_user = request.user
        total_person = int(request.POST['person'])
        booking_id = str(room_id) + str(datetime.datetime.now())

        booking = Booking()
        room_object = Room.objects.all().get(id=room_id)
        room_object.status = '2'
        
        user_object = User.objects.all().get(username=current_user)

        booking.customer = user_object
        booking.room = room_object
        person = total_person
        booking.check_in = request.POST['check_in']
        booking.check_out = request.POST['check_out']
        booking.save()
        messages.success(request,"Congratulations! Booking Successfull")
        return redirect("my-booking")
    else:
        return HttpResponse('Access Denied')

@login_required
def my_booking(request):
    """
    View function for displaying user's bookings.
    Requires the user to be logged in.
    """
    if request.user.is_authenticated == False:
        return redirect('home')
    user = User.objects.all().get(id=request.user.id)
    bookings = Booking.objects.all().filter(customer=user)
    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'my_booking.html',{'bookings':bookings}))


@login_required
def edit_booking(request, booking_id):
    """
    View function for editing a booking.
    Requires the user to be logged in.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully")
            return redirect("my-booking")
    else:
        form = BookingForm(instance=booking)
    
    return render(request, "edit_booking.html", {"form": form, "booking": booking})


@login_required
def delete_booking(request, booking_id):
    """
    View function for deleting a booking.
    Requires the user to be logged in.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    messages.success(request, "Booking deleted successfully")
    return redirect("my-booking")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.send_email()
                request.session['user_name'] = form.cleaned_data['name']
                return redirect('success_url')
            except Exception as e:
                messages.error(request, f"Failed to send email: {str(e)}")
                return render(request, 'contact.html', {'form': form})
        else:
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

def success_view(request):
    name = request.session.get('user_name', 'Guest')
    return render(request, 'success.html', {'user_name': name})