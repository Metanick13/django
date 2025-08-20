from django.http import HttpResponse

def index(request):
    return HttpResponse("Алисик и евка лучшие подружки")
