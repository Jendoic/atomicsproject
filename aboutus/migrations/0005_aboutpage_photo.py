# Generated by Django 5.0.2 on 2024-03-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0004_alter_corevalue_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='photo',
            field=models.ImageField(blank=True, upload_to='staffPhotos/'),
        ),
    ]
