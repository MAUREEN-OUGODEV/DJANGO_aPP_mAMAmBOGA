from django import forms
from .models import Signup

class SignUploadForm(forms.ModelForm):
    class Meta:
        model= Signup
        fields ="__all__"