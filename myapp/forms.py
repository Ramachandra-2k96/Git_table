from django import forms
class submit_form(forms.Form):
    input_file = forms.FileField()