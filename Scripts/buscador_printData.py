import ast
import json
from random import choice

archivo_pags = open('Salidas/items_pageRanking.json','r').read().encode('utf-8').decode('utf-8','ignore')
pageRankArchivo = json.loads(archivo_pags)
keysSorted = sorted(pageRankArchivo, key=lambda k: pageRankArchivo[k]['ranking'], reverse=True)
pageIndex = 0
print('\n************************Lista Ordenada por Ranking**************************\n')
for itemSorted in keysSorted:
    pageIndex+=1
    itemData = pageRankArchivo[itemSorted]
    itemRanking = str(itemData['ranking'])
    contenido = open(itemData['ruta'].replace("html","txt"),'r', encoding="utf8").read()[:140].strip().replace("\n"," ")
    print('\t No.%s - titulo: %s \n' % (pageIndex, itemData['titulo']))
    print('\t\t Contenido: \n')
    print('\t\t %s \n' % contenido)
    print('\t\t Url:%s \n' % itemSorted)
    print('\t\t Relevancia de búsqueda: %s \n' % itemRanking)
    print('\t\t Ranking de página: %s \n' % itemRanking)
print('\n________________________Desarrollado por Jeffrey Cortés________________________\n')
