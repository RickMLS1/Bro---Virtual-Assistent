from clima.obter_clima import obter_clima
from microfone.ouvir_microfone import ouvir_microfone
from responder.responder_pergunta import responder_pergunta
from falar.falar import falar

# O restante do código do assistente_virtual() vai aqui
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
        else:
            falar("Desculpe, não entendi. Poderia repetir ou fazer outra pergunta?")
            pergunta = ouvir_microfone()
            responder_pergunta(pergunta)
