from django.db import models


# Create your models here.
class ContactInfo(models.Model):
    organisation_email = models.EmailField()
    organisation_contact = models.CharField(max_length=15)
    location = models.CharField()


class UserContact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.firstname
