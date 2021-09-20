from django import forms
import datetime
from django.forms.fields import ChoiceField, IntegerField
from django.utils.text import slugify
import datetime


class InputDataForm(forms.Form):

    GENDER_EDUCATION = [(0 , 'Male'),
        (1 , 'Female'),]
        
    VEHICLE_AGE = [('100' , 'Less than 1 year'),
        ('010' , '1 to 2 Years'),
        ('001' , 'Greater than two years'),]
    
    

    gender = forms.ChoiceField(choices=GENDER_EDUCATION)
    age = forms.IntegerField()
    holds_driving_license = forms.BooleanField(required=False)
    previously_insured = forms.BooleanField(required=False)
    vehicle_age = forms.ChoiceField(choices=VEHICLE_AGE)
    is_vehicle_damaged = forms.BooleanField(required=False)
    annual_premium = forms.IntegerField()
    policy_sales_channel = forms.IntegerField()
    vintage = forms.IntegerField()

