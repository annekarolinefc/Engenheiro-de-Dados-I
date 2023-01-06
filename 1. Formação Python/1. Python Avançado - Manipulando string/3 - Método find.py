# O método find retorna o índice

argumento = "moedaorigem=real"
index = argumento.find('=')
print(f'Index do sinal =: {index}')
substring = argumento[index+1:]
print(f'Palavra após o sinal=: {substring}')


#-----------------------------------------------------

celular = "(41)96574-1728"
#Buscando indice
indiceInicialCodigoArea=celular.find("(")+1
indiceFinalCodigoArea=celular.find(")")

print(celular[indiceInicialCodigoArea:indiceFinalCodigoArea])

