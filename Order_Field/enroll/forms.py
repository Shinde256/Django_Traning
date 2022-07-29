from django import forms

class Student_Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()