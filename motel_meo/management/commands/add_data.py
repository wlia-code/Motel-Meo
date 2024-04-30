from django.core.management.base import BaseCommand
from motel_meo.models import Hotel, Room

class Command(BaseCommand):
    help = 'Adds sample data to the database'

    def handle(self, *args, **kwargs):
        hotel1 = Hotel.objects.create(name='Royal', location='Galmla', state='Stockholm')
        room1 = Room.objects.create(room_type='1', status='1', price=100.00, capacity=2, size=200, room_no=101, hotel=hotel1)
        
        self.stdout.write(self.style.SUCCESS('Data added successfully'))
