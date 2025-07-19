from django.contrib import admin
from .models import *

@admin.register(Vulnerability)
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('nightlord', 'damage', 'value')
    list_filter = ('nightlord',)
    search_fields = ('nightlord', 'damage')

@admin.register(Loot)
class LootAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

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
    list_display = ('name', 'min_level', 'recommended_level')
    list_filter = ('min_level',)
    search_fields = ('name',)

@admin.register(Nightlord)
class NightlordAdmin(admin.ModelAdmin):
    list_display = ('name', 'expedition', 'main_weakness')
    list_filter = ('main_weakness',)
    search_fields = ('name',)
