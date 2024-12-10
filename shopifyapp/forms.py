from django import forms
from shopifyapp.models import VehicleReport, LoginForms, CreateForm, ImageModel


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = VehicleReport
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginForms
        fields = '__all__'

class CreateForms(forms.ModelForm):
    class Meta:
        model = CreateForm
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'
