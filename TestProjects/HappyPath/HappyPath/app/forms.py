from django import forms

class HappyPathForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=50)
    age = forms.IntegerField(label='Age', min_value = 10, max_value=100)

class SadPathForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=50)
    age = forms.IntegerField(label='Age', min_value = 10, max_value=100)

class SuperForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=50, min_length=2, initial='Your name', required=False )
    #somethingelse = forms.BooleanField(label='boolean test', required=False)
    dateStuff = forms.DateField(label='thedate')
    decimalStuff = forms.DecimalField(label='decimalstuff', max_value=4224.2, min_value=23, max_digits=23, decimal_places=2)
    floatStuff = forms.FloatField(label='floatstuff', max_value=1223, min_value=12)
    genericIpAddress = forms.GenericIPAddressField(label='ipaddress', protocol='ipv4')
    TimeFields = forms.TimeField(label='timesstuff', input_formats='%H:%M:%S')
    URLFields = forms.URLField(label='urlstuff', max_length=123, min_length=12)

