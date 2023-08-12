from django import forms
from .models import Sign_in

class SignUploadForm(forms.ModelForm):
    class Meta:
        model= Sign_in
        fields ="__all__"