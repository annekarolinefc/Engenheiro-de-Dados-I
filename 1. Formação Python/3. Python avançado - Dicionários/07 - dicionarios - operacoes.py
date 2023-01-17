## MAPA - DICIONÁRIO
aparicoes = dict(Guilherme = 2, cachorro = 1)
aparicoes2 = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo":1
}

print(aparicoes)
print(type(aparicoes))

print('\nAparições:')
print(aparicoes2)
print(type(aparicoes2))

print("\nAdicionando elemento no dicionário:")
aparicoes2['Carlos'] = 1
print(aparicoes2)

print("\nSubstituindo valor em um elemento no dicionário:")
aparicoes2['Carlos'] = 2
print(aparicoes2)

print("\nRemovendo elemento no dicionário:")
del aparicoes2['Carlos']
print(aparicoes2)

print("\nElemento esta dentro do dicionario? :")
print("cachorro" in aparicoes2)
print("Carlos" in aparicoes2)

print("\nImprimindo cada elemento:")
for elemento in aparicoes2:
    print(elemento)

print("\nImprimindo valor de cada elemento:")
for elemento in aparicoes2.values():
    print(elemento)

print("\nValor 1 está em valor de algum elemento:")
print(1 in aparicoes2.values())

print("\nImprimindo elemento e valor de cada elemento:")
for elemento in aparicoes2.keys():
    print(elemento, aparicoes2[elemento])

print("\nImprimindo usando items e exibindo tuplas:")
for elemento in aparicoes2.items():
    print(elemento)

print('\n')