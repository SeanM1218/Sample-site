from django import forms

class RegisterPatient(forms.Form):
    name = forms.CharField(label="Patient Name", max_length=200)