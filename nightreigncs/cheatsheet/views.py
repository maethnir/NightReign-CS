from django.shortcuts import render
from .models import Location, Nightfarer, Expedition

def viewer_page(request):
    locations = Location.objects.all().order_by('min_level')
    nightfarers = Nightfarer.objects.all()
    expeditions = Expedition.objects.prefetch_related("Nightlords__weaknesses__damage", "Nightlords__main_weakness")

    nightlord_data = {}
    expedition_data = {}

    for ex in expeditions:
        expedition_data[ex.id] = {
            "name": ex.name,
            "icon_url": ex.icon.url
        }
        nightlords = []
        for nl in ex.Nightlords.all():
            nightlords.append({
                "name": nl.name,
                "main_weakness": {
                    "name": nl.main_weakness.name if nl.main_weakness else "None",
                    "icon_url": nl.main_weakness.icon.url if nl.main_weakness and nl.main_weakness.icon else ""
                },
                "vulnerabilities": [
                    {
                        "name": vuln.damage.name,
                        "icon_url": vuln.damage.icon.url if vuln.damage.icon else "",
                        "is_condition": vuln.damage.is_condition,
                        "value": vuln.value
                    } for vuln in nl.weaknesses.all()
                ]
            })
        nightlord_data[ex.id] = nightlords

    return render(request, 'cheatsheet.html', {
        'locations': locations,
        'nightfarers': nightfarers,
        'expeditions': expeditions,
        'expedition_data': expedition_data,
        'nightlord_data': nightlord_data
    })
