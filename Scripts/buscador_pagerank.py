import ast
import json
import io
from random import choice

numPalabras = "5000"
archivo_pags = open('Salidas/items_indexed.json','r').read().encode('utf-8').decode('utf-8','ignore')
pageRankArchivo = json.loads(archivo_pags)
dkeys = list(pageRankArchivo.keys())
seedel = dkeys[0] #choice(dkeys)
seed = pageRankArchivo[seedel]
seedflag = False

def depurar_enlaces(enlaces):
    dkeysEnlacesFinal = enlaces[:]
    pageIndex = 0
    splitBar = "/"
    for item in enlaces:
        itemSplit = list(filter(None, item.split(splitBar)))
        dominio = "https://en.wikipedia.org"
        Itemvalue = dominio + item if itemSplit[0] == "wiki" else item
        #print("urlRelativa: %s" %  urlRelativa )
        index = dkeysEnlacesFinal.index(item)
        if Itemvalue not in dkeys:
            #print("item next->" + item)
            del dkeysEnlacesFinal[index]
            #print("Eliminado index->" + str(index)+ " ->" + item)
        else:
            dkeysEnlacesFinal[index] = Itemvalue
        pageIndex += 1
    #print("for count-> " + str(pageIndex))
    dkeysEnlacesFinal = dkeysEnlacesFinal if len(dkeysEnlacesFinal) > 0  else []
    return dkeysEnlacesFinal

while not seedflag:
    enlaces = seed['enlaces']
    #print("item next->" + seedel + " before len:" + str(len(enlaces)))
    #Se ejecuta función para depurar los enlaces que no encuentran
    #dentro del listado de paginas principal (dkeys)
    enlaces = depurar_enlaces(enlaces)
    if seedel in dkeys:
        pageRankArchivo[seedel]['enlaces'] = enlaces
    #print("item next->" + seedel + " current len:" + str(len(enlaces)))
    seed['ranking'] = seed['ranking'] + 1
    seed['enlaces'] = enlaces
    numItems = len(enlaces)
    if numItems > 0:
        dkeysEnlaces = seed['enlaces']
        nextseedel = choice(dkeysEnlaces)
        seedel = nextseedel
        if nextseedel in dkeys:
            seed = pageRankArchivo[nextseedel]
    else:
        seedel = choice(dkeys)
        seed = pageRankArchivo[seedel]
    if seed['ranking'] > len(dkeys):
    	seedflag = True
with open('Salidas/items_pageRanking.json', 'w') as outfile:
    json.dump(pageRankArchivo, outfile)
    outfile.close()
