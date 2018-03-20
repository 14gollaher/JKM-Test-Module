from django import forms

class HappyPathForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=50)
    age = forms.IntegerField(label='Age', min_value = 10, max_value=100)

class SadPathForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=50)
    age = forms.IntegerField(label='Age', min_value = 10, max_value=100)
    horses = forms.IntegerField(label='Horses', min_value = 1000)
