import django
import os
import pandas as pd

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nightreigncs.settings")  # Replace with your project's settings module
django.setup()
from cheatsheet.models import *
from django.db import IntegrityError

data = pd.read_csv("nightreigncs/SPREAD.csv", sep=";")
damages = [col for col in data.columns if col != "Nightlord"]

for index, row in data.iterrows():
    nightlord = Nightlord.objects.filter(name=row["Nightlord"]).first()
    if nightlord is not None:
        for damage in damages:
            try:
                vil, _created = Vulnerability.objects.get_or_create(
                    nightlord = nightlord,
                    damage = Damage.objects.filter(name=damage).first(),
                    value = row[damage]
                )
            except Exception as err:
                print(f"Error. Nightlord: {nightlord} damage: {damage}.\nError: {err}")
            if _created:
                print(f"Added vulnerability to {damage} for {nightlord.name}")