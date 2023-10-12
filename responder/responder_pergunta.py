from googlesearch import search
from falar.falar import falar
from microfone.ouvir_microfone import ouvir_microfone

# Aqui serão adicionadas respostas pré-definidas para perguntas frequentes.
def responder_pergunta(pergunta): 
    # Adicione aqui a lógica para responder a perguntas específicas.
    # Resposta para uma pergunta específica:
    if "qual o maior clube do brasil" in pergunta:
        falar("A capital do Brasil é Brasília.")
    else:
        pesquisar_web(pergunta)     

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
