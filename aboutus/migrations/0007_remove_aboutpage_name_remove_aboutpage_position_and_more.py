# Generated by Django 5.0.2 on 2024-03-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0006_aboutpage_name_aboutpage_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='position',
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='names',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='positions',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
