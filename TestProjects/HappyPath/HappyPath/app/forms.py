from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class SadPathForm(forms.Form):
    helper = FormHelper()
    helper.label_class = 'col-xs-5 col-sm-5 col-md-5 col-lg-5'
    helper.field_class = 'col-xs-5 col-sm-5 col-md-4 col-lg-3'
    firstName = forms.CharField(label='First name', max_length=50)
    age = forms.IntegerField(label='Age', min_value = 10, max_value=100)
    helper.layout = Layout(
        Div(
            Div('firstName'),
            Div('age'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
            ),
        css_class='row'),
    )

class SuperForm(forms.Form):
    helper = FormHelper()
    helper.label_class = 'col-xs-5 col-sm-5 col-md-5 col-lg-5'
    helper.field_class = 'col-xs-5 col-sm-5 col-md-4 col-lg-3'
    Name = forms.CharField(label='Full Name', max_length=50, min_length=2, initial='Your name', required=False )
    Float = forms.FloatField(label='Weight', max_value=1223, min_value=12, required=True)
    Decimal = forms.DecimalField(label='Income', max_value = 4224.2, min_value=23, max_digits=10, decimal_places=2)
    Integer = forms.IntegerField(label='Age', min_value = 10, max_value=100)
    Date = forms.DateField(label='Date of Birth')
    IpAddress = forms.GenericIPAddressField(label='Your IP Address', protocol='ipv4')
    Time = forms.TimeField(label='Time of Day', input_formats='%H:%M:%S')
    Url = forms.URLField(label='Favorite Website', max_length=123, min_length=12)    
    helper.layout = Layout(
        Div(
            Div('Name'),
            Div('Date'),
            Div('Decimal'),
            Div('Integer'),
            Div('Float'),
            Div('IpAddress'),
            Div('Time'),
            Div('Url'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
            ),
        css_class='row'),
    )

class ClassForm(forms.Form):
    helper = FormHelper()
    helper.label_class = 'col-xs-5 col-sm-5 col-md-5 col-lg-5'
    helper.field_class = 'col-xs-5 col-sm-5 col-md-4 col-lg-3'
    firstName = forms.CharField(label='First name', max_length=20, min_length=3, initial='Your name', required=False )
    dateStuff = forms.DateField(label='Date')
    decimalStuff = forms.DecimalField(label='Decimal Number', max_value=4224.2, min_value=23, max_digits=23, decimal_places=2)
    floatStuff = forms.FloatField(label='Float Number', max_value=1223, min_value=3)
    genericIpAddress = forms.GenericIPAddressField(label='IP Address', protocol='ipv4')
    TimeFields = forms.TimeField(label='Time', input_formats='%H:%M:%S')
    URLFields = forms.URLField(label='URL', max_length=123, min_length=12)
    helper.layout = Layout(
        Div(
            Div('firstName'),
            Div('dateStuff'),
            Div('decimalStuff'),
            Div('floatStuff'),
            Div('genericIpAddress'),
            Div('TimeFields'),
            Div('URLFields'),
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
            ),
        css_class='row'),
    )

