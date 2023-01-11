email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 esse é o meu celular"

"""
O numero pode estar no final, no meio ou no inicio da string.
Maaaas, a estrutura do numero do telefone é padronizada.
4 digitos + - + 4 digitos
"""

# varia de 0 ate 9
padrao = "[0123456789]"
# como eu preciso de 4
padrao = "[0123456789][0123456789][0123456789][0123456789]"
# mais um digito [-]
padrao = "[0123456789][0123456789][0123456789][0123456789][-]"
# mais 4 digitos
padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"

# Importando a biblioteca
import re 
# recebe o padrão que quero encontrar e onde irei buscar
retorno = re.search(padrao, email1)
print(retorno)
# retorna so o resultado
print(retorno.group())


retorno = re.search(padrao, 'lalalalalalala 4687-8790 hahahaha')
print(retorno.group())

#---------------------------------------------------
padrao_re = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"
# recebe o padrão que quero encontrar e onde irei buscar
retorno = re.search(padrao_re, email1)
# retorna so o resultado
print(retorno.group())

#-----------------------------------------
#{4,5} busca intervalos
padrao_re = "[0-9]{4,5}[-][0-9][0-9][0-9][0-9]"
# recebe o padrão que quero encontrar e onde irei buscar
retorno = re.search(padrao_re, email1)
# retorna so o resultado
print(retorno.group())

#----------------------------------------
# retorne todos -> re.findall()
#{4,5} busca intervalos
#{4} busca so 4 digitos
padrao_re = "[0-9]{4,5}[-][0-9]{4}"
# recebe o padrão que quero encontrar e onde irei buscar
retorno = re.findall(padrao_re, 'lalala 98976-0989 e de 4 digitios 6776-0989 lalala 26378-8293 lalala')
# retorna so o resultado
print(retorno)

#-----------------------------------------
padrao = "e[0-9]{1,2} [s,t][0-9]{1,2}"
conversa1 = "Estou no e 1 t 3 de Naruto"
conversa2 = "O e02 t2 é o melhor de Rick and Morty"
conversa3 = "Eu parei GOT no e2 s3"
conversa4 = "Não gostei do ep4 t5 de Vikings"
conversa5 = "O melhor episódio de Boku no Hero é o e011 s02"

retorno_1 = re.search(padrao,conversa1)
retorno_2 = re.search(padrao,conversa2)
retorno_3 = re.search(padrao,conversa3)
retorno_4 = re.search(padrao,conversa4)
retorno_5 = re.search(padrao,conversa5)
# retorna so o resultado
print(retorno_1)
print(retorno_2)
print(retorno_3)
print(retorno_4)
print(retorno_5)
