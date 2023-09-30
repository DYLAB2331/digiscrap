from django import forms
from django.contrib.auth.models import User
from .models import Photo

class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "description", "date"]

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )
