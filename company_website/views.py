from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, ContactMessage

# Create your views here.

def home(request):
    return render(request, 'company_website/home.html')

def about(request):
    return render(request, 'company_website/about.html')

def services(request):
    services_list = Service.objects.all()
    return render(request, 'company_website/services.html', {'services_list': services_list})

def contact(request):
    if request.method == 'POST':
        name = (request.POST.get('name') or '').strip()
        email = (request.POST.get('email') or '').strip()
        phone = (request.POST.get('phone') or '').strip()

        if not name or not email or not phone:
            messages.error(request, 'Пожалуйста, заполните все обязательные поля.')
            return render(request, 'company_website/contact.html', {
                'form_data': {
                    'name': name,
                    'email': email,
                    'phone': phone,
                }
            })

        ContactMessage.objects.create(name=name, email=email, phone=phone)
        messages.success(request, 'Спасибо! Ваше сообщение отправлено.')
        return redirect('contact')

    return render(request, 'company_website/contact.html')

def personal_cabinet(request):
    return render(request, 'company_website/personal_cabinet.html')


def payment(request):
    return render(request, 'company_website/payment.html')


# Service detail pages
def service_apartment_security(request):
    return render(request, 'company_website/services/apartment_security.html')


def service_cottage_security(request):
    return render(request, 'company_website/services/cottage_security.html')


def service_business_security(request):
    return render(request, 'company_website/services/business_security.html')


def service_car_security(request):
    return render(request, 'company_website/services/car_security.html')


def service_fire_alarm(request):
    return render(request, 'company_website/services/fire_alarm.html')


def service_access_control(request):
    return render(request, 'company_website/services/access_control.html')


def service_sensors(request):
    return render(request, 'company_website/services/sensors.html')


def service_physical_security(request):
    return render(request, 'company_website/services/physical_security.html')


def service_panic_button(request):
    return render(request, 'company_website/services/panic_button.html')


def service_monitoring(request):
    return render(request, 'company_website/services/monitoring.html')


def promotions(request):
    return render(request, 'company_website/promotions.html')


def reviews(request):
    return render(request, 'company_website/reviews.html')


def requisites(request):
    return render(request, 'company_website/requisites.html')
