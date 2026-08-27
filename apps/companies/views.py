from django.http import HttpResponse


def companies(request):
    return HttpResponse("Hello, world. This is company app")