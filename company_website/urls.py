from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('personal-cabinet/', views.personal_cabinet, name='personal_cabinet'),
    path('payment/', views.payment, name='payment'),
    path('promotions/', views.promotions, name='promotions'),
    path('reviews/', views.reviews, name='reviews'),
    path('requisites/', views.requisites, name='requisites'),
    # services detail
    path('services/apartment-security/', views.service_apartment_security, name='service_apartment_security'),
    path('services/cottage-security/', views.service_cottage_security, name='service_cottage_security'),
    path('services/business-security/', views.service_business_security, name='service_business_security'),
    path('services/car-security/', views.service_car_security, name='service_car_security'),
    path('services/fire-alarm/', views.service_fire_alarm, name='service_fire_alarm'),
    path('services/access-control/', views.service_access_control, name='service_access_control'),
    path('services/sensors/', views.service_sensors, name='service_sensors'),
    path('services/physical-security/', views.service_physical_security, name='service_physical_security'),
    path('services/panic-button/', views.service_panic_button, name='service_panic_button'),
    path('services/monitoring/', views.service_monitoring, name='service_monitoring'),
]
