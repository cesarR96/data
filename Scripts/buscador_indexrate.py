from bs4 import BeautifulSoup
import json
import os
import io

numPalabras = "5000"
archivo_pags = open('Salidas/items.json','r').read()
pageRankArchivo = json.loads(archivo_pags)
lista_pags = list(pageRankArchivo.keys())
pags_index = 0
# Ciclo para leer todos las páginas
for url_act in lista_pags:
    print("***********Inicio")
    path = pageRankArchivo[url_act]['ruta']
    print("url actual-> " + path)
    nombreArchivo = ""
    with io.open(pageRankArchivo[url_act]['ruta'],'r',encoding='utf8') as f:
        body = f.read()
        nombreArchivo = f.name
    soup = BeautifulSoup(body, "html.parser")
    for script in soup(["script","style"]):
      script.extract()
    texto_completo = soup.get_text()
    #Se revisa si existe la carpeta para escribir los archivos y sino se crea la carpeta
    carpeta = 'Salidas/Paginas_txt'
    if not os.path.exists(carpeta):
      os.makedirs(carpeta)
    #Se captura el titulo de la página y se escribe el archivo con el texto plano
    titulo = nombreArchivo.replace("Salidas/Paginas_html/pag_", "").replace(".html","")
    archivo = nombreArchivo.replace("html", "txt")
    print("titulo->" + titulo)
    with io.open(archivo, 'w', encoding = 'utf8') as f:
        textoSinCarEsp = texto_completo.translate({ord(c): " " for c in "↑!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        listaPalabras = textoSinCarEsp.split()
        f.write(textoSinCarEsp.replace('\n',' '))
        f.close()
    #Se inicia captura de frecuencia de palabras
    frecPalabras = {}
    for palabra in listaPalabras:
        frecPalabras[palabra] = listaPalabras.count(palabra)
    pageRankArchivo[url_act]['titulo'] = titulo
    pageRankArchivo[url_act]['palabras'] = frecPalabras
    pags_index += 1
    print('Páginas indexadas: '+ str(pags_index))
#Escribir el archivo json
with io.open('Salidas/items_indexed.json','w',encoding='utf8') as archivo_pagerankfinal:
    archivo_pagerankfinal.write(json.dumps(pageRankArchivo))
    archivo_pagerankfinal.close()
