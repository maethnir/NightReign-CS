from django.shortcuts import render
from .models import *

def viewer_page(request):
    locations = Location.objects.all().order_by('recommended_level')
    nightfarers = Nightfarer.objects.all()
    expeditions = Expedition.objects.all().order_by('display_order')
    all_events = Event.objects.all()
    events = all_events.filter(is_shifting_earth=False)
    shifting_earth = all_events.filter(is_shifting_earth=True)

    return render(request, 'cheatsheet.html', {
        'locations': locations,
        'nightfarers': nightfarers,
        'expeditions': expeditions,
        'events': events,
        'shifting_earth': shifting_earth
    })
