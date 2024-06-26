from googlesearch import search
import speech_recognition as sr
import pyttsx3
import pyaudio
import requests
import webbrowser

def ouvir_microfone():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        reconhecedor.adjust_for_ambient_noise(source)
        audio = reconhecedor.listen(source)

    try:
        print("Reconhecendo...")
        texto = reconhecedor.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("Desculpe, não consegui entender o áudio.")
    except sr.RequestError as e:
        print(f"Ocorreu um erro durante o reconhecimento de fala; {e}")

    return ""

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

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

def pesquisar_web(query):
    try:
        resultados = search(query, num_results=3, lang='pt')
        if resultados:
            print("Aqui estão alguns resultados da pesquisa:")
            for i, resultado in enumerate(resultados, start=1):
                print(f"Resultado {i}: {resultado}")
        else:
            print("Desculpe, não encontrei nenhum resultado para essa pesquisa.")
    except Exception as e:
        print("Desculpe, ocorreu um erro ao realizar a pesquisa.")

def reproduzir_musica(musica):
    query = musica.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def responder_pergunta(pergunta):  
    if "qual a capital do brasil?" in pergunta:
        falar("A capital do Brasil é Brasília.")
    else:
        pesquisar_web(pergunta)

def assistente_virtual():
    falar("Olá! Sou o Bro. Como posso ajudar?")
    
    while True:
        comando = ouvir_microfone().lower()
        
        if "valeu" in comando:
            falar("Tranquilo meu parceiro!")
            break
        elif "clima" in comando:
            falar("Claro! Para qual cidade você deseja saber o clima?")
            cidade = ouvir_microfone()
            obter_clima(cidade)
        elif "tocar música" in comando:
            falar("Claro! Qual música você gostaria de ouvir?")
            musica = ouvir_microfone()
            falar(f"Reproduzindo {musica} no YouTube.")
            reproduzir_musica(musica)
        else:
            falar("Desculpe, não entendi. Poderia repetir ou fazer outra pergunta?")
            pergunta = ouvir_microfone()
            responder_pergunta(pergunta)
        

if __name__ == "__main__":
    assistente_virtual()
