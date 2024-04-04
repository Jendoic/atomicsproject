from django.db import models


# Create your models here.
class LandingPage(models.Model):
    title = models.CharField()
    subtitle = models.TextField()
    body = models.TextField()
    discipleship = models.TextField()
    development = models.TextField()
    philosophy = models.TextField()

    def __str__(self):
        return self.title
