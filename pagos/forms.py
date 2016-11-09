from django import forms
from django.forms import Form
from django.conf import settings

from .models import Donation, CardType, Donnor
from .payment_template import form_parametros
from pagos.email import send_thanks_email

import paypalrestsdk
import simplejson
import json


class DonationForm(Form):
    first_name = forms.CharField(
        label='Name',
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control form-white', 'placeholder': 'Name'}))
    last_name = forms.CharField(
        label='Last Name',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control form-white', 'placeholder': 'Last Name'}))
    mail = forms.EmailField(
        max_length=150,
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control form-white', 'placeholder': 'Email'}))
    card_type = forms.ModelChoiceField(
        required=True,
        label='',
        queryset=CardType.objects.all(),
        widget=forms.HiddenInput(attrs={'class': 'form-control form-white dropdown', 'placeholder': ''}))
    number = forms.CharField(
        max_length=20,
        label='Card number',
        widget=forms.TextInput(attrs={'class': 'form-control form-white', 'placeholder': 'Card number'}))
    expire_month = forms.IntegerField(
        help_text='2 digits',
        label='Month',
        widget=forms.NumberInput(attrs={'class': 'form-control form-white', 'placeholder': 'Month (XX)'}))
    expire_year = forms.IntegerField(
        help_text='4 digits',
        label='Year',
        widget=forms.NumberInput(attrs={'class': 'form-control form-white', 'placeholder': 'Year (XXXX)', 'size': 4, 'maxlength': 4}))
    cvv2 = forms.CharField(
        label='CVV',
        max_length=4, widget=forms.NumberInput(attrs={'class': 'form-control form-white', 'placeholder': 'CVV'}))
    total = forms.DecimalField(
        label='Donation ($)',
        max_digits=7, decimal_places=2, min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control form-white', 'placeholder': 'Donation ($)'}))

    def clean(self):
        cleaned_data = super(DonationForm, self).clean()
        if cleaned_data.get("card_type") is None:
            raise forms.ValidationError("Error processing your card. Please check it is a valida number.")
        paypalrestsdk.configure({
            "mode": settings.PP_MODE,
            "client_id": settings.PP_CLIENT_ID,
            "client_secret": settings.PP_CLIENT_SECRET})
        credit_card = {
            "type": cleaned_data.get("card_type").card_type,
            "number": cleaned_data.get("number"),
            "expire_month": cleaned_data.get("expire_month"),
            "expire_year": cleaned_data.get("expire_year"),
            "cvv2": cleaned_data.get("cvv2"),
            "first_name": cleaned_data.get("first_name"),
            "last_name": cleaned_data.get("last_name")}
        payment = paypalrestsdk.Payment(form_parametros(credit_card, simplejson.dumps(cleaned_data.get("total"))))
        if payment.create():
            donnor = Donnor.objects.create(
                first_name=cleaned_data.get("first_name"),
                last_name=cleaned_data.get("last_name"),
                mail=cleaned_data.get("mail"),)
            donnor.save()
            donation = Donation.objects.create(
                card_type=cleaned_data.get("card_type"),
                total=cleaned_data.get("total"),
                donnor=donnor,
                payment_ref=payment.id)
            donation.save()
            if 'EMAIL_FROM' in globals():
                send_thanks_email(cleaned_data.get("first_name"), cleaned_data.get("last_name"), cleaned_data.get("mail"), cleaned_data.get("total"))
            print("Payment[%s] created successfully" % (payment.id))
        else:
            print(payment.error)
            err_text = ""
            if "details" in payment.error:
                err_text = "Error given was: "
                for err in payment.error['details']:
                    err_text += err['issue'] + " "
            raise forms.ValidationError("Error during payment due to invalid credit card. Please check your credentials." + err_text)
