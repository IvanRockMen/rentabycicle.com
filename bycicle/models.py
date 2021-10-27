from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.fields import CharField

# Create your models here.


class BycicleCompany(models.Model):
    company_name = CharField("Company name", max_length=45)

    def __str__(self):
        return self.company_name

class Bycicle(models.Model):
    #owner = ForeignKey(BaseUser)
    bycicle_company = ForeignKey(BycicleCompany, on_delete=models.CASCADE)
