from django.contrib import admin

from .models import ContactInfo, UserContact

# Register your models here.
admin.site.register(ContactInfo)
admin.site.register(UserContact)
