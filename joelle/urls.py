"""joelle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView


from django.contrib.auth.decorators import login_required
from blood.views import   IndexView, HospitalCreateView, OrderCreateView, DonorCreateView, OrderListView, DonorListView, HospitalListView, HospitalUpdateView, DonorUpdateView, OrderUpdateView, HospitalDeleteView, DonorDeleteView, OrderDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name = 'home' ),
    

    #authentications
    path('login/',LoginView.as_view(), name="login"),  
    #path('logout/', LogoutView.as_view(), name="logout"),
#

    #creations
    path('new_hospital/', HospitalCreateView.as_view(), name= 'new_hospital'),
    path('new_order/', OrderCreateView.as_view(), name= 'new_order'),
    path('new_donator/', DonorCreateView.as_view(), name= 'new_donator'),


    #listes
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('hospital_list/', HospitalListView.as_view(), name='hospital_list'),
    path('donator_list/', DonorListView.as_view(), name='donor_list'),

    #les modifications
    path('hospital_update/<int:pk>/', HospitalUpdateView.as_view(), name='hospital_update'),
    path('order_update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('donor_update/<int:pk>/', DonorUpdateView.as_view(), name='donor_update'),

    #les suppressions
    path('hospital_delete/<int:pk>/delete/', HospitalDeleteView.as_view(), name='hospital_delete' ),
    path('order_delete/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete' ),
    path('donor_delete/<int:pk>/delete/', DonorDeleteView.as_view(), name='donor_delete' ),
]
