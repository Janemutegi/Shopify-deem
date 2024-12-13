from django import forms
from shopifyapp.models import VehicleReport, LoginForms


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = VehicleReport
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginForms
        fields = '__all__'

