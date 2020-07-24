from django import forms
from .models import  Donors, Hospital, Order
from django.forms import ModelForm



class DonorCreateForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = ['name', 'blood_type', 'gender', 'phone', 'address']

class HospitalCreateForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'address', 'phone', 'email']

class OrderCreateForm(forms.ModelForm):
    OPTIONS = (
        ('',''),
        ('Postpay','Postpay'),
        ('Prepay (Full)','Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Ready', 'Ready'),
        ('Send', 'Send'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = Order
        fields = ['partner','phone','address','delivery_date','product','payment_option', 'quantity','price','status']
