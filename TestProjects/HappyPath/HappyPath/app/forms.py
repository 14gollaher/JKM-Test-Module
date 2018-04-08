from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class HappyPathForm(forms.Form):
    firstName = forms.CharField(label='First name', max_length=50)
    age = forms.IntegerField(label='Age', min_value = 10, max_value=100)

class SadPathForm(forms.Form):
    helper = FormHelper()
    helper.label_class = 'col-sm-2 col-xs-5 col-sm-offset-4'
    helper.field_class = 'col-sm-2 col-xs-5'
    firstName = forms.CharField(label='First name', max_length=50)
    age = forms.IntegerField(label='Age', min_value = 10, max_value=100)
    dog = forms.IntegerField(label='Age', min_value = 10, max_value=100)
    helper.layout = Layout(
        Field('firstName'),
        Field('age'),
        Field('dog'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
        )
    )
class SuperForm(forms.Form):
    helper = FormHelper()
    helper.label_class = 'col-sm-2 col-xs-5 col-sm-offset-4'
    helper.field_class = 'col-sm-2 col-xs-5'
    firstName = forms.CharField(label='First name', max_length=50, min_length=2, initial='Your name', required=False )
    dateStuff = forms.DateField(label='thedate')
    decimalStuff = forms.DecimalField(label='decimalstuff', max_value = 4224.2, min_value=23, max_digits=23, decimal_places=2)
    floatStuff = forms.FloatField(label='floatstuff', max_value=1223, min_value=12)
    genericIpAddress = forms.GenericIPAddressField(label='ipaddress', protocol='ipv4')
    TimeFields = forms.TimeField(label='timesstuff', input_formats='%H:%M:%S')
    URLFields = forms.URLField(label='urlstuff', max_length=123, min_length=12)    
    helper.layout = Layout(
        Field('firstName'),
        Field('dateStuff'),
        Field('decimalStuff'),
        Field('floatStuff'),
        Field('genericIpAddress'),
        Field('TimeFields'),
        Field('URLFields'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
        )
    )
class ClassForm(forms.Form):
    helper = FormHelper()
    helper.label_class = 'col-sm-2 col-xs-5 col-sm-offset-4'
    helper.field_class = 'col-sm-2 col-xs-5'
    firstName = forms.CharField(label='First name', max_length=20, min_length=3, initial='Your name', required=False )
    dateStuff = forms.DateField(label='thedate')
    decimalStuff = forms.DecimalField(label='decimalstuff', max_value=4224.2, min_value=23, max_digits=23, decimal_places=2)
    floatStuff = forms.FloatField(label='floatstuff', max_value=1223, min_value=3)
    genericIpAddress = forms.GenericIPAddressField(label='ipaddress', protocol='ipv4')
    TimeFields = forms.TimeField(label='timesstuff', input_formats='%H:%M:%S')
    URLFields = forms.URLField(label='urlstuff', max_length=123, min_length=12)
    helper.layout = Layout(
        Field('firstName'),
        Field('dateStuff'),
        Field('decimalStuff'),
        Field('floatStuff'),
        Field('genericIpAddress'),
        Field('TimeFields'),
        Field('URLFields'),
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
        )
    )

