from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Main Page")

def error_404(request, extention):
    data = {}
    return HttpResponse("Error 404")
    #return render(request, "main/error404.html", data)

def error_403(request, extention):
    data = {}
    return HttpResponse("Error 403")
    #return render(request, "main/error403.html", data)

def error_400(request, extention):
    data = {}
    return HttpResponse("Error 400")
    #return render(request, "main/error400.html", data)

def error_500(request):
    data = {}
    return HttpResponse("Error 500")
    #return render(request, "main/error500.html", data)
