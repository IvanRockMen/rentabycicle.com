from django.urls import path
from . import views


app_name = 'bycicle'

urlpatterns = [
    path('', views.index, name= "main"),
    path('new/', views.new, name="new"),
    path('<int:bycicle_id>/', views.bycicle, name="bycicle"),
    path('add/', views.add, name="add")
]
