idades = [15, 87, 39, 29, 51, 11, 29]
tamanho_lista = len(idades)
range_lista = range(len(idades)) # intervalo

for idade in idades:
    print(idade)

print('\n')

for i in range(len(idades)):
    print(i)

print('\n')

for i in range(len(idades)):
    print(i, idades[i])

print('\n')

print(list(enumerate(idades)))

print('\n')

# desempacotando
for indice, idade in enumerate(idades):
    print(indice, idade)

print('\n')

# desempacotando e exibindo somente um
for indice, idade in enumerate(idades):
    print(idade)

print('\n')

# desempacotando, ignorando o resto
for indice, _ in enumerate(idades):
    print(indice)