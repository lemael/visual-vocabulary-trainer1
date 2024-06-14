from django import forms

from .models import PdfFile

class PdfForm(forms.ModelForm):
    class Meta:
        model = PdfFile
        fields = ('pdf_file', 'title')

        widgets = {
            'pdf_file': forms.FileInput(attrs={'class': 'form-control w-20'}),
            'title': forms.TextInput(attrs={'class': 'form-control w-20'})
        }