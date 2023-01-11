import re
# Essa expressão regular funciona de pega todas as possibilidades de "a" até "z" 
# repetidos até 20 vezes, pega um espaço em branco e após isso pega 2 número em seguida a letra "h"
padrao = "[a-z]{1,20}[ ][0-9]{1,2}[h]"
frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"

retorno_1 = re.search(padrao,frase1)
retorno_2 = re.search(padrao,frase2)
retorno_3 = re.search(padrao,frase3)

print(retorno_1) # sabado 23h
print(retorno_2) # quinta 21h
print(retorno_3) # terca 19h