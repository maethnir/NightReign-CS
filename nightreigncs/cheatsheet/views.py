from django.shortcuts import render
from .models import Location, Nightfarer, Nightlord

def viewer_page(request):
    locations = Location.objects.all()
    nightfarers = Nightfarer.objects.all()
    nightlords = Nightlord.objects.select_related('main_weakness').prefetch_related('weaknesses__damage')

    # Prepare JS-safe nightlord data
    nightlord_data = {
        nl.id: {
            'main_weakness': {
                'name': nl.main_weakness.name,
                'icon_url': nl.main_weakness.icon.url
            },
            'vulnerabilities': [
                {
                    'name': vuln.damage.name,
                    'percent': vuln.percent,
                    'icon_url': vuln.damage.icon.url
                } for vuln in nl.weaknesses.all()
            ]
        } for nl in nightlords
    }

    return render(request, 'base.html', {
        'locations': locations,
        'nightfarers': nightfarers,
        'nightlords': nightlords,
        'nightlord_data': nightlord_data,
    })
