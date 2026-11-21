from django.db import models

#payment model
class paymentModel(models.Model):
    cardholder_name = models.CharField(max_length=55)
    card_num = models.CharField(max_length=16)
    card_type = models.CharField(max_length=25)
    card_cvc = models.CharField(max_length= 3)
    card_expire_date = models.DateField(null=False, default="00/00")
    address_1 = models.CharField(max_length=16)
    address_2 = models.CharField(max_length=16)
    postcode = models.CharField(max_length=12)
    
#appointment booking model
class appointmentModel(models.Model):
    customer_name = models.CharField(max_length=55)
    appointment_type = models.CharField(max_length=12)
    appointment_date = models.DateField(null=False, default="00/00/0000")
    appointment_time = models.TimeField(null= False, default="00:00")
    appointment_status = models.CharField(max_length=9)
    appointment_cancelled = models.BooleanField(default=False)

#carbon calculation model
class carbonModel(models.Model):
    co2_data = models.IntegerField()
    co2_emmissions = models.IntegerField()
    result = models.IntegerField(null=True)

#energy usage model
class energyusageModel(models.Model):
    power_usage = models.IntegerField()
    time_on = models.TimeField()
    power_result = models.IntegerField()