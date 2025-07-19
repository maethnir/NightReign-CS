from django.contrib import admin
from .models import Damage, Nightfarer, Location, Nightlord

@admin.register(Damage)
class DamageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Nightfarer)
class NightfarerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_level')
    list_filter = ('min_level',)
    search_fields = ('name',)

@admin.register(Nightlord)
class NightlordAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_weakness')
    list_filter = ('main_weakness',)
    search_fields = ('name',)
