from django.shortcuts import render, redirect
from .models import Hotel, Room, Booking
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SearchForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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


def sign_up(request):
    """
    View function for user registration.
    Handles the registration form submission and creates a new user.
    """
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                messages.warning(request, "Passwords didn't match")
                return redirect('https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/login/')
            try:
                if User.objects.get(username=user_name):
                    messages.warning(request, "Username not available")
                    return redirect('https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/login/')
            except User.DoesNotExist:
                pass
            new_user = User.objects.create_user(username=user_name, password=password1)
            new_user.is_superuser = False
            new_user.is_staff = False
            new_user.save()
            messages.success(request, "Registration successful")
            return redirect("https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/login/")
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})

def log_in(request):
    """
    View function for user login.
    Handles the login form submission and authenticates the user.
    """
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/') 
        else:
            messages.warning(request, "Incorrect username or password")
            return redirect('https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/login/')

    return render(request, 'login.html')

def log_out(request):
    """
    View function for user logout.
    Logs out the authenticated user and redirects to the home page.
    """
    if request.method =='GET':
        logout(request)
        messages.success(request,"Logged out successfully")
        print("Logged out successfully")
        return redirect('https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/')
    else:
        print("logout unsuccessfull")
        return redirect('https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/login/')

@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def book_room(request):
    if request.method == "POST":
        room_id = request.POST.get('room_id')
        room = Room.objects.get(id=room_id)
        
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        if room.is_available(check_in, check_out):
            booking = Booking.objects.create(
                room=room,
                customer=request.user,
                check_in=check_in,
                check_out=check_out
            )

            room.status = '2'
            room.save()

            messages.success(request, "Congratulations! Booking Successful")
            return redirect("https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/")
        else:
            messages.warning(request, "Sorry, This Room is unavailable for Booking")
            return redirect("https://8000-wliacode-motelmeo-yrw1ssbaeih.ws-eu110.gitpod.io/")
    else:
        return HttpResponse('Access Denied')

