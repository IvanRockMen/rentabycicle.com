from django.core.exceptions import ObjectDoesNotExist
from django.http import response
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from code.base_view import base_view
from main.views import error_404
from .models import Bycicle


# Create your views here.
@base_view
def index(request):
    try:
        bycicle = Bycicle.objects.order_by('-bycicle_company')[:10]
    except ObjectDoesNotExist as e:
        bycicle = None
    return render(request, 'bycicle/index.html', {"bycicles": bycicle})

@base_view
def new(request):
    return render(request, 'bycicle/new.html')

@base_view
def bycicle(request, bycicle_id:int):
    try:
        bycicle = Bycicle.objects.get(id = bycicle_id)
    except ObjectDoesNotExist as e:
        return HttpResponseNotFound(error_404(request, str(e)))
    return render(request, 'bycicle/bycicle.html', {"bycicle": bycicle})

@base_view
def add(request):
    pass
