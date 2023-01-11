url = 'www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar'
print(len(url))

index = url.find("moedaOrigem")
print(index)

substring=url[index:]
print(substring)

nome = 'Eren Yeager'
tamanho = len(nome)
print(f'\nTamanho do nome {nome} = {tamanho}')
indice = nome.find('Eren')
print(tamanho)
print(f'O nome {nome} começa na posição {indice}')
print(nome[indice:tamanho])