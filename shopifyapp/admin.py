from django.contrib import admin

from shopifyapp.models import Subscribe, Register, VehicleReport, LoginForms

# Register your models here.
admin.site.register(Subscribe)
admin.site.register(Register)
admin.site.register(VehicleReport)

admin.site.register( LoginForms)




