from django import forms


class CarForm(forms.Form):
    brand1 = forms.CharField(label='Марка авто', max_length=10)
    producer1 = forms.CharField(label='Производитель', max_length=10)
    year1 = forms.IntegerField(label='Год выпуска', min_value=1900, max_value=2023)
    number1 = forms.CharField(label='Гос.номер', max_length=9)
