# Generated by Django 5.2.4 on 2025-07-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheatsheet', '0003_remove_nightlord_display_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='min_level',
        ),
        migrations.AlterField(
            model_name='location',
            name='recommended_level',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]
