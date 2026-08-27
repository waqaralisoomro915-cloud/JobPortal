from django.http import HttpResponse

def candidates(request):
    return HttpResponse("Candidates, this is candidates app")