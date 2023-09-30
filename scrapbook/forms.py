from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["image", "description", "date"]

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )