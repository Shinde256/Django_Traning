from django import forms

class Student_Registration(forms.Form):
    name = forms.CharField(widget=forms.FileInput)