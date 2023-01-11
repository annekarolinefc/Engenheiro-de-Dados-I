import re
padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
# Vamos testar esse padrão.
texto =  "Meu número para contato é 2633-5723"
retorno = re.search(padrao,texto)
print(retorno.group())

# SIMPLIFICANDO O PADRAO
padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
padrao = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"
padrao = "[0-9]{4}[-][0-9]{4}"
padrao = "[0-9]{4}-[0-9]{4}" #Para deixar nosso padrão mais simples podemos retirar [-] e deixar somente -, pois essa é a única opção para essa posição.
padrao = "[0-9]{4,5}-[0-9]{4}" #caso o número de telefone seja de um celular e possua um 9 na frente do número? Podemos dar opções para os quantificadores.

# se quisermos que o - seja opcional dentro da expressão regular? Uma forma de fazer isso é utilizando o operador ?
padrao = "[0-9]{4,5}-?[0-9]{4}"
texto =  "Meu número para contato é 26335723"
retorno = re.search(padrao,texto)
print(retorno.group())