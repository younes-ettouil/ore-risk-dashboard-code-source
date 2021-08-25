from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(npv_total)
admin.site.register(npv_Counterparty)
admin.site.register(dates)