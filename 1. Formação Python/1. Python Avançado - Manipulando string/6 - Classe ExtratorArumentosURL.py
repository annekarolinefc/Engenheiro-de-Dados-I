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

url = 'www.bytebank.com.br/cambio?`valor=1500&moedaOrigem=real&moedaDestino=dolar'
argumento = ExtratorArgumentosURL(url)
print(argumento)

