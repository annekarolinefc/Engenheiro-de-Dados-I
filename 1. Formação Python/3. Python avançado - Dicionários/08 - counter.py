texto = "Bem vindo meu nome é Elias irei falar sobre os meus gostos eu gosto muito de cachorros e gatos eu gosto também de beber café"
texto = texto.lower()
print(texto)

# Utilizando a api
from collections import Counter
aparicoes = Counter(texto.split())
print(aparicoes)

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    print("{} => {:.2f}%".format(caractere, proporcao * 100))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


analisa_frequencia_de_letras(texto)