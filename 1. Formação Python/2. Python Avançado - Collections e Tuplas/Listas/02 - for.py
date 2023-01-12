print('*'*10)
print("Imprimindo Listas")
print('*'*10)

idades = [1, 20, 34, 2, 34, 9]
print(idades)

print("\nIterando uma lista...")
for idade in idades:
    print(idade)

print("\nAdicionando 4 aos elementos")
for idade in idades:
    print(idade+4)

print("\nIdades no ano que vem")
idades_no_ano_que_vem=[]
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)
    print(idades_no_ano_que_vem)
print(f"\nLista completa: {idades_no_ano_que_vem}\n")