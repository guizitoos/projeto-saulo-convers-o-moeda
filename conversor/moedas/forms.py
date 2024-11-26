from django import forms

class ConversorForm(forms.Form):
    de_moeda = forms.CharField(max_length=3, label='De (moeda)')
    para_moeda = forms.CharField(max_length=3, label='Para (moeda)')
    valor = forms.FloatField(label='Valor')
    from django import forms

MOEDAS_CHOICES = [
    ('USD', 'Dólar Americano (USD)'),
    ('EUR', 'Euro (EUR)'),
    ('BRL', 'Real Brasileiro (BRL)'),
    ('JPY', 'Iene Japonês (JPY)'),
    ('GBP', 'Libra Esterlina (GBP)'),
]

class ConversorForm(forms.Form):
    de_moeda = forms.ChoiceField(choices=MOEDAS_CHOICES, label='De (moeda)')
    para_moeda = forms.ChoiceField(choices=MOEDAS_CHOICES, label='Para (moeda)')
    valor = forms.FloatField(label='Valor')

#moedas_choice é as opções de moedas disponíveis para conversão[
    
#classe ConversorForm é os campos do formulario 
