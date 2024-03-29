from django.urls import path

from .views import ContactFormView, ContactDone

urlpatterns = [
    path("", ContactFormView.as_view(), name="contact"),
    path("contact_done/", ContactDone.as_view(), name="contact_done"),
]
