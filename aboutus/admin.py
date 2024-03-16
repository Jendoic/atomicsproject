from django.contrib import admin
from .models import AboutPage, CoreValue


# Register your models here.
class CoreValueInline(admin.TabularInline):
    model = CoreValue


class AboutPageAdmin(admin.ModelAdmin):
    inlines = [
        CoreValueInline,
    ]
    list_display = ["title"]


# autocomplete_fields = ("values",)


admin.site.register(AboutPage, AboutPageAdmin)
