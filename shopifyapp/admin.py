from django.contrib import admin

from shopifyapp.models import Subscribe, Register, WebsiteContent, VehicleReport, LoginForms, CreateForm, ImageModel

# Register your models here.
admin.site.register(Subscribe)
admin.site.register(Register)
admin.site.register(VehicleReport)
admin.site.register(WebsiteContent)
admin.site.register( LoginForms)
admin.site.register( CreateForm)
admin.site.register(ImageModel)


