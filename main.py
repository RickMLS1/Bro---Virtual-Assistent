import speech_recognition as sr
import pyttsx3
import pyaudio
import requests

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

def assistente_virtual():
    falar("Olá! Sou o Bro. Como posso ajudar?")
    
    while True:
        comando = ouvir_microfone().lower()
        
        if "bom dia" in comando:
            falar("Bom dia, gato, vamos começar o show?")

        elif "clima" in comando:
            falar("Claro! Para qual cidade você deseja saber o clima?")
            cidade = ouvir_microfone()
            obter_clima(cidade)
        # Adicione aqui as respostas e ações do assistente virtual com base nos comandos detectados.
        # Por exemplo, você pode adicionar lógica para responder a perguntas específicas, fornecer informações,
        # executar cálculos, definir lembretes, etc.
        elif "parar" in comando:
            falar("Tranquilidade, lindo, até mais!")
            break
        

if __name__ == "__main__":
    assistente_virtual()
