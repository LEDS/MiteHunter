from django import forms


class UploadFieldForm(forms.Form):
    title = forms.CharField(max_length=50)
    File = forms.FileField()