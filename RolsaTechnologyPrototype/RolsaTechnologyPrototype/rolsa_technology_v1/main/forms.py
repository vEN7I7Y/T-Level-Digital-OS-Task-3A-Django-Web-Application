from django.forms import ModelForm

from .models import *

#class to initialise the payment form
class paymentForm(ModelForm):
    class Meta:
        model = paymentModel
        fields = "__all__"

#class to initialise the appointment form
class appointmentForm(ModelForm):
    class Meta:
        model = appointmentModel
        exclude = ["appointment_id", "appointment_status", "appointment_cancelled"]

#class to initialise the carbon data form
class carbonForm (ModelForm):
    class Meta:
        model = carbonModel
        exclude = ["result"]

#class to initialise the energy usage form
class energy_usageForm(ModelForm):
    class Meta:
        model = energyusageModel
        exclude = ["power_result"]