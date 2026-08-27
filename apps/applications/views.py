from django.http import HttpResponse

def applications(request):
    return HttpResponse("Hello, world. this is applications app")