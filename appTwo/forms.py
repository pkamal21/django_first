from django import forms


class Signup(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()
    text = forms.CharField(widget=forms.Textarea)
