from django.db import models

class Damage(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='Damage')

class Nightfarer(models.Model):
    name = models.CharField(max_length=25)
    summary = models.ImageField(upload_to='Nightfarers')

class Location(models.Model):
    name = models.CharField(max_length=25)
    min_level = models.PositiveSmallIntegerField(default=2)
    image = models.ImageField(upload_to='Locations')

class Nightlord(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='Nightlords')
    main_weakness = models.ForeignKey(Damage, on_delete=models.PROTECT)

class Vulnerability(models.Model):
    nightlord = models.ForeignKey(Nightlord, on_delete=models.CASCADE, related_name="weaknesses")
    damage = models.ForeignKey(Damage, on_delete=models.CASCADE)
    percent = models.SmallIntegerField(default=0)