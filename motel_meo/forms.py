from django import forms
from .models import Hotel,Booking
from django.utils import timezone
class SearchForm(forms.Form):
    """
    Form for searching hotel rooms based on location, check-in date, check-out date, and capacity.
    """
    search_location = forms.ModelChoiceField(
        queryset=Hotel.objects.all(), 
        empty_label="Select a location",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    check_in = forms.DateField(
        label="Check-in Date", 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': timezone.now().date()})
    )
    check_out = forms.DateField(
        label="Check-out Date", 
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': timezone.now().date()})
    )
    capacity = forms.IntegerField(
        label="Capacity",
        min_value=0, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_in < timezone.now().date():
            self.add_error('check_in', 'Check-in date cannot be in the past.')

        if check_out and check_out < timezone.now().date():
            self.add_error('check_out', 'Check-out date cannot be in the past.')

        if check_in and check_out and check_in > check_out:
            self.add_error('check_out', 'Check-out date cannot be before the check-in date.')



class UserRegistrationForm(forms.Form):
    """
    Form for user registration with username and password fields.
    """
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in', 'check_out']
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if check_in and check_in < timezone.now().date() and 'check_in' in self.changed_data:
            self.add_error('check_in', 'Check-in date cannot be in the past.')

        if check_out and check_out < timezone.now().date() and 'check_out' in self.changed_data:
            self.add_error('check_out', 'Check-out date cannot be in the past.')



class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # Logic to send email
        from django.core.mail import send_mail
        subject = f"Message from {self.cleaned_data['name']}"
        message = self.cleaned_data['message']
        sender = self.cleaned_data['email']
        recipients = ['wasimalrawas9@gmail.com']
        send_mail(subject, message, sender, recipients, fail_silently=False)