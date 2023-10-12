import speech_recognition as sr

# O restante do código da função ouvir_microfone() vai aqui
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
