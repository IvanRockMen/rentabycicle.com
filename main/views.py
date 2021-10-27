from django.http.response import HttpResponse
from django.shortcuts import render

from code.base_view import base_view

# Create your views here.
@base_view
def index(request):
    return render(request, 'main/index.html')

@base_view
def error_404(request, exception):
    return render(request, "main/error404.html")

@base_view
def error_403(request, exception):
    return render(request, "main/error403.html")

@base_view
def error_400(request, exception):
    return render(request, "main/error400.html")

@base_view
def error_500(request):
    return render(request, "main/error500.html")
