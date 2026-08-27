from django.http import HttpResponse

def common(request):
    return HttpResponse("Hello, world. this is common app")