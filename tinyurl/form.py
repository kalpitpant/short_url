from django import forms

class InputForm(forms.Form):
    url = forms.URLField(max_length= 200)
    
