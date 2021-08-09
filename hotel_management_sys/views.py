from django.shortcuts import render
from .models import Room


# Create your views here.
def homepage(request):
    print('this is the request', request)

    all_rooms_qs = Room.objects.all()

    return render(request, 'homepage.html', {
        'name': 'Django',
        'rooms': all_rooms_qs
    })
