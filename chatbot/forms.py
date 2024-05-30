from django import forms
from .widgets import MultipleFileInput

class UploadPDFForm(forms.Form):
    pdfs = forms.FileField(widget=MultipleFileInput, required=True)

class QuestionForm(forms.Form):
    question = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ask your question here...'}))