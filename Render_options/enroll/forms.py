from django import forms

class Student_Registration(forms.Form):
    name = forms.CharField(label='your name',label_suffix=':-',initial='Sudhir',disabled=True,help_text='Limiu 30 character')
