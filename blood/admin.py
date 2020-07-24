from django.contrib import admin
from . models import Blood,Donors,Hospital, Order
from .forms import  DonorCreateForm, HospitalCreateForm, OrderCreateForm



class DonorCreateAdmin(admin.ModelAdmin):
   list_display = ['name', 'blood_type', 'gender', 'phone', 'address']
   form = DonorCreateForm
   list_filter = ['blood_type']
   search_fields = ['blood_type']

class HospitalCreateAdmin(admin.ModelAdmin):
   list_display = ['name', 'address', 'phone', 'email']
   form =HospitalCreateForm
   list_filter = ['name']
   search_fields = ['name']



admin.site.register(Blood)
admin.site.register(Hospital, HospitalCreateAdmin)
admin.site.register(Order)
admin.site.register(Donors, DonorCreateAdmin)
