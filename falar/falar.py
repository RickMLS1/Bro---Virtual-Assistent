import pyttsx3

# O restante do código da função falar() vai aqui
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
