usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [12, 23, 56, 42]

assistiram = []
print(f'Assistiram: {assistiram}')
#assistiram.extend(usuarios_data_science)
assistiram = usuarios_data_science.copy()
print(f'Assistiram: {assistiram}')
assistiram.extend(usuarios_machine_learning)
print(f'Assistiram: {assistiram}')

# REMOVER DUPLICADAS
print(set(assistiram))

print(set(1, 2, 3, 4, 4, 4, 3, 2, 1))
