from django.contrib import admin
from .models import *

admin_payment = paymentModel
admin_appointment = appointmentModel
admin_carbon = carbonModel
admin_energy_usage = energyusageModel


admin.site.register(admin_payment)
admin.site.register(admin_appointment)
admin.site.register(admin_carbon)
admin.site.register(admin_energy_usage)
