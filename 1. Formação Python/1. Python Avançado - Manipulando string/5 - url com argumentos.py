url = 'www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar'

#pagina?arumentos
pagina = url[:27]
argumento=url[26:]
print(f"URL completa: {url}\nPagina: {pagina}\nArgumento:{argumento}")

# UTILIZANDO FIND - mais usual - ATENDE A TODOS OS PROJETOS
find=url.find('?')
pagina_find=url[:find]
argumento_find=url[find+1:]
print(f"URL completa: {url}\nPagina: {pagina_find}\nArgumento:{argumento_find}")