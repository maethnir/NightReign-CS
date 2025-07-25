from django.db import models

class Damage(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='Damage')
    is_condition = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Loot(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='Loot')

    class Meta:
        verbose_name = "Loot"
        verbose_name_plural = "Loot"

    def __str__(self):
        return self.name

class Nightfarer(models.Model):
    name = models.CharField(max_length=25)
    summary = models.ImageField(upload_to='Nightfarers')

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=25)
    recommended_level = models.PositiveSmallIntegerField(default=5)
    image = models.ImageField(upload_to='Locations')
    contains = models.ManyToManyField(Loot, blank=True)

    def __str__(self):
        return self.name

    def loot(self):
        return list(self.contains)

class Expedition(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to='Expeditions')
    display_order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Nightlord(models.Model):
    name = models.CharField(max_length=50)
    main_weakness = models.ForeignKey(Damage, on_delete=models.SET_NULL, null=True)
    expedition = models.ForeignKey(Expedition, on_delete=models.PROTECT, null=True, related_name="Nightlords")

    def __str__(self):
        return self.name

class Vulnerability(models.Model):
    nightlord = models.ForeignKey(Nightlord, on_delete=models.CASCADE, related_name="weaknesses")
    damage = models.ForeignKey(Damage, on_delete=models.CASCADE)
    value = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = "Vulnerability"
        verbose_name_plural = "Vulnerabilities"

    def __str__(self):
        return f"{self.nightlord} - {self.damage}"

class Event(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.TextField()
    long_description = models.TextField()
    rewards = models.ManyToManyField(Loot, blank=True)
    is_shifting_earth = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class Walkthrough(models.Model):
    parent_event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="steps")
    step = models.PositiveSmallIntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="Walkthrough")
    description = models.TextField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["step", "parent_event"], name='unique_walkthrough_step')
        ]

    def __str__(self):
        return f"{self.parent_event} - Step {self.step}"
