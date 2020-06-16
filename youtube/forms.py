from django import forms

class linkForm(forms.Form):
    link = forms.CharField(label='Vedio Link', max_length=100)