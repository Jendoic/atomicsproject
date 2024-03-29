from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    message = forms.CharField(label="message", widget=forms.Textarea)
