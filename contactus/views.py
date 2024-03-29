from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


from .models import ContactInfo, UserContact


# Create your views here.
class ContactDone(TemplateView):
    template_name = "contactpages/contact_done.html"


class ContactFormView(CreateView):
    model = UserContact
    fields = [
        "firstname",
        "lastname",
        "message",
    ]
    template_name = "contactpages/contact.html"
    success_url = reverse_lazy("contact_done")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contactinfo = ContactInfo.objects.first()

        if contactinfo:
            context["organisation_email"] = contactinfo.organisation_email
            context["organisation_contact"] = contactinfo.organisation_contact
            context["location"] = contactinfo.location
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Add placeholder to firstname
        form.fields["firstname"].widget.attrs["placeholder"] = "Enter your first name"
        form.fields["lastname"].widget.attrs["placeholder"] = "Enter your last name"
        form.fields["message"].widget.attrs[
            "placeholder"
        ] = "Share with us your message"

        return form
