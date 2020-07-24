from django.shortcuts import render, redirect
from .models import Order, Donors, Hospital
from .forms import OrderCreateForm , DonorCreateForm, HospitalCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_hopitaux'] = Hospital.objects.all().count()
        context['total_donateur'] = Donors.objects.all().count()
        context['total_commande'] = Order.objects.all().count()
        return context

# creations

class HospitalCreateView(CreateView):
    form_class = HospitalCreateForm
    template_name = 'new_hospital.html'
    success_url = reverse_lazy('home')

class OrderCreateView(CreateView):
    form_class = OrderCreateForm
    template_name = 'new_order.html'
    success_url = reverse_lazy('home')

class DonorCreateView(CreateView):
    form_class = DonorCreateForm
    template_name = 'new_donator.html'
    success_url = reverse_lazy('home')

# lists
class HospitalListView(ListView):
    template_name = 'hospital_list.html'
    model = Hospital


class DonorListView(ListView):
    template_name = 'donor_list.html'
    model = Donors


class OrderListView(ListView):
    template_name = 'order_list.html'
    model = Order


# les modifications

class HospitalUpdateView(UpdateView):
    model = Hospital
    template_name = 'new_hospital.html'
    fields = ['name', 'address', 'phone', 'email']
    success_url = reverse_lazy('hospital_list')

class DonorUpdateView(UpdateView):
    model = Donors
    template_name = 'new_donator.html'
    fields = ['name', 'blood_type', 'phone' , 'gender', 'address']
    success_url = reverse_lazy('donor_list')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'new_order.html'
    fields = ['partner', 'phone', 'address', 'product' , 'quantity', 'payment_option', 'price']
    success_url = reverse_lazy('hospital_list')


#les suppressions

class HospitalDeleteView (DeleteView):
    template_name = 'confirm_delete.html'
    model = Hospital
    success_url = reverse_lazy('hospital_list')

class DonorDeleteView (DeleteView):
    template_name = 'confirm_delete.html'
    model = Donors
    success_url = reverse_lazy('donor_list')

class OrderDeleteView (DeleteView):
    template_name = 'confirm_delete.html'
    model = Order
    success_url = reverse_lazy('order_list')



#authentication



