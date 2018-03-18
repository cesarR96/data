import scrapy
import os
import wikipedia
import json
from WebCrawler.items import pagInfo

class LinksSpider(scrapy.Spider):
    name = "wiki_links"
    start_urls = []
    def __init__(self):
        cadenaTexto = input('Por favor ingresa el texto que deseas buscar en la fuente de Wikipedia.com: ');
        resultados = wikipedia.search(cadenaTexto, results = 20)
        print(resultados)
        for result in resultados:
            try:
                page = wikipedia.page(result)
                self.start_urls.append(page.url)
            except wikipedia.exceptions.DisambiguationError as e:
                print ("Error: {} ".format(result))
                continue
            except wp.exceptions.PageError:
                #We've tried to find a page that doesn't exist
                print ("The page {} could not be found".format(result))
                continue
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        #Comando para guardar página que no esté mapeada aún
        pagina = response.url.split("/")[-1]
        carpeta = "Salidas/Paginas_html"
        #Se evalua si ya existe la carpeta
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        nombre_archivo = carpeta + '/pag_%s.html' % pagina
        with open(nombre_archivo, 'wb') as f:
            f.write(response.body)
            self.log('Archivo %s guardado' % nombre_archivo)
        #Comando para crear el objeto pagInfo
        infoPagina = pagInfo()
        infoPagina['url'] = response.url
        infoPagina['enlaces'] = response.css('a::attr(href)').extract()
        infoPagina['ruta'] = nombre_archivo
        yield infoPagina
