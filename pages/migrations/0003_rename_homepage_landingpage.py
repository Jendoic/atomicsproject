# Generated by Django 5.0.2 on 2024-04-04 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_homepage_delete_page'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePage',
            new_name='LandingPage',
        ),
    ]
