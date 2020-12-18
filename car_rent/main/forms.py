from django import forms
from main.models import OrderData




class OrderDataForm(forms.ModelForm):
    class Meta:
        model = OrderData
        fields = ('name', 'surname', 'phone_number', 'passport_first','passport_second',
                  'driver_lisense_first','driver_lisense_second')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'label': 'Имя',
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия и Отчество',
                'label': 'Фамилия и Отчество',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона',
                'id':'phonenumber',
                'label': 'Номер телефона(формат: 7 999 999 99 99)',
            }),
        }