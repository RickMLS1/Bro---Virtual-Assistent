import requests
from falar.falar import falar

# O restante do código da função obter_clima() vai aqui
def obter_clima(cidade):
    chave_api = "0d08ade5e3fa06c027beafbf0e199e80"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"
    resposta = requests.get(url)
    dados = resposta.json()
    
    if dados["cod"] == 200:
        clima = dados["weather"][0]["description"]
        temperatura = dados["main"]["temp"]
        falar(f"O clima em {cidade} está {clima} com temperatura de {temperatura:.1f} graus Celsius.")
    else:
        falar("Não foi possível obter as informações sobre o clima. Por favor, tente novamente mais tarde.")
