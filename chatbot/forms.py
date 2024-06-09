from django import forms
from .widgets import MultipleFileInput

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class UploadPDFForm(forms.Form):
    chapter_name = forms.CharField(max_length=100)
    chapter_number = forms.ChoiceField(choices=[(i, str(i)) for i in range(1, 6)])
    pdfs = forms.FileField(widget=MultipleFileInput(attrs={'class': 'form-control', 'multiple': True}), required=True)
class QuestionForm(forms.Form):
    question = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ask your question here...'}))