from django.shortcuts import render
from .models import Location, Nightfarer, Expedition, Nightlord

def viewer_page(request):
    locations = Location.objects.all().order_by('min_level')
    nightfarers = Nightfarer.objects.all()
    expeditions = Expedition.objects.all()

    return render(request, 'cheatsheet.html', {
        'locations': locations,
        'nightfarers': nightfarers,
        'expeditions': expeditions
    })
