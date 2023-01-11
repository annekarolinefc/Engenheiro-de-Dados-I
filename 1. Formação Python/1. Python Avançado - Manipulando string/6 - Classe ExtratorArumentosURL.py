class ExtratorArgumentosURL:
    """def __init__(self, url):
        self.url = url"""
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError("URL inválida!!!")
            
    def urlEhValida(self, url):
        if url:
            return True
        else:
            return False

    def ExtrairArgumentos(self):
        indiceInicialMoedaDestino = self.url.find("=", 15)+1

        indiceInicialMoedaOrigem = self.url.find("=")+1
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino:]

url = 'www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar'
argumento = ExtratorArgumentosURL(url)
print(argumento)

moedaOrigem, moedaDestino = argumento.ExtrairArgumentos()
print(moedaOrigem, moedaDestino)

