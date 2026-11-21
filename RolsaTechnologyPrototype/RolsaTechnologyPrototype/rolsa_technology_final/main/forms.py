from django.forms import ModelForm
from django import forms
from .models import *


# class to initialise the payment form
class paymentForm(forms.ModelForm):
    class Meta:
        model = paymentModel
        fields = "__all__"
        # sets up the widgets for use in the template
        widgets = {
            "card_num": forms.PasswordInput(),
            "card_cvc": forms.PasswordInput(),
            "card_expire_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }


# class to initialise the appointment form
class appointmentForm(ModelForm):
    appointment_type_value = [
        ("installation", "Installation £20"),
        ("appointment", "Appointment £15"),
    ]
    booking_type = forms.ChoiceField(choices=appointment_type_value)

    class Meta:
        model = appointmentModel
        exclude = ["appointment_id", "appointment_status", "appointment_cancelled"]
        # sets up the widgets for use in the template
        widgets = {
            "booking_type": forms.Select(),
            "appointment_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "appointment_time": forms.TimeInput(
                attrs={
                    "type": "time",
                }
            ),
        }


# class to initialise the carbon data form
class carbonForm(ModelForm):
    class Meta:
        model = carbonModel
        exclude = ["result"]


# class to initialise the energy usage form
class energy_usageForm(ModelForm):
    class Meta:
        model = energyusageModel
        exclude = ["power_result"]
