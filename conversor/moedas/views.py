import requests #lembrar de importar o requests na faculdade pip install requests
from django.shortcuts import render
from .forms import ConversorForm
from .models import Conversao

#peguei a API da ExchangeRate.host
API_KEY = "34d611b71eb2c24b47cf92e261d05470"  #COLOCAR UMA CHAVE DE API NOVA CASO NÃO FUNCIONE

def conversor_view(request):
    resultado = None
    erro = None  
    
    simbolos = {
        "BRL": "R$",  
        "USD": "$",   
        "EUR": "€",   
        "GBP": "£",   
        "JPY": "¥",   
        
    }
    
    if request.method == 'POST':
        form = ConversorForm(request.POST) #é para verificar se os dados enviados são validos
        if form.is_valid():
            de_moeda = form.cleaned_data['de_moeda'].upper()
            para_moeda = form.cleaned_data['para_moeda'].upper()  #esses 3 são para pegar os dados do formulario
            valor = form.cleaned_data['valor']
            url = f"https://api.exchangerate.host/convert?from={de_moeda}&to={para_moeda}&amount={valor}&access_key={API_KEY}"
            
            try:
                response = requests.get(url) #chama a api
                response.raise_for_status()  
                data = response.json()
                print("Resposta da API:", data)

                if data.get('success', False):
                    resultado = data.get('result', None)
                    
                    if resultado is None:
                        erro = "Erro ao obter taxa de câmbio."
                    else:
                        resultado_numero = float(resultado)  
                        simbolo_de_moeda = simbolos.get(de_moeda, "")
                        simbolo_para_moeda = simbolos.get(para_moeda, "")
                        if para_moeda == "JPY":
                            simbolo_para_moeda = "¥"  
                        
                        Conversao.objects.create(
                            de_moeda=de_moeda,
                            para_moeda=para_moeda, 
                            valor=valor,
                            resultado=resultado_numero  
                        )
                        
                        resultado_com_simbolo = f"{simbolo_para_moeda} {resultado_numero:,.2f}"
                else:
                    erro = f"Erro na resposta da API. Detalhes: {data.get('error', 'Não especificado')}"
            except requests.exceptions.RequestException as e:
                erro = f"Erro ao conectar à API: {e}"
    else:
        form = ConversorForm()

    return render(request, 'moedas/conversor.html', {
        'form': form,
        'resultado': resultado_com_simbolo if resultado else None, 
        'erro': erro
    })

def historico_view(request):
    historico = Conversao.objects.all().order_by('-data')  
    return render(request, 'moedas/historico.html', {'historico': historico})
