import uuid
from django.db import models
from django.urls import reverse


# Create your models here.
class AboutPage(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField()
    body = models.CharField()
    vision = models.CharField()
    mission = models.CharField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("aboutpage_detail", args=[str(self.id)])


class CoreValue(models.Model):
    aboutpage = models.ForeignKey(
        AboutPage,
        on_delete=models.CASCADE,
        related_name="values",
    )
    values = models.CharField()

    def __str__(self):
        return self.values
