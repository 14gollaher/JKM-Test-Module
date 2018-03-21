from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    someDeciaml = models.DecimalField('somename', 'ok', 123, 3)
    duration = models.DurationField()
    #commaone = models.CommaSeparatedIntegerField(12)
    #Datefeld = models.DateField('no', 'no', False, False)
    #DateTiemfeld = models.DateTimeField(False, False)
    emailfeld = models.EmailField(254)
    floatfeld = models.FloatField()
    integerfeld = models.IntegerField()
    ipfeld = models.GenericIPAddressField('no','no', 'both', False)
    #nullboolfeld = models.NullBooleanField()
    #slugfeld = models.SlugField(50)
    #timefeld = models.TimeField('no','no', False,False)

