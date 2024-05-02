from django import forms
class busForm(forms.Form):
    busNo=forms.CharField(max_length=30)

class mailForm(forms.Form):
    mail=forms.EmailField()