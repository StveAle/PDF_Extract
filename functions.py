import fitz
from datetime import datetime
import os

#retorna un string con la fecha/hora del sistema, 
# se usa para evitar duplicados en archivos
def now():
    fecha=datetime.now()
    now=fecha.strftime('%d-%m-%Y-%H-%M-%S')
    return now

#Verifica si una carpeta ya está creada, si no es así la crea
def checkCreateFile(nameFile):
  try: os.mkdir(nameFile)
  except: pass
  location=f'./{nameFile}'
  return location

#De una lista de palabras a buscar en un PDF retorna una lista de coords
def ccWords(listWords,pdfAdress):

    file=fitz.open(pdfAdress)
    coord=[]

    for i, page in enumerate(file.pages(), start=1):
        coord.append(f'page: {i}')
        pageword=page.get_text('words')
        for word in pageword:
            if word[4] in listWords:
                coord.append(word)

    return coord

#Guarda elementos de una lista en un txt
def saveListTxt(lista):
    ahora=now()
    with open(f"./file_{ahora}.txt", "w") as output:
        for row in lista:
            output.write(str(row)+'\n')

#Devuelve un string a partir de una frase y dos strings de referencia que
#delimitan el inicio y el fin del string. No toma los string de incio y fin.
#Nota: el código es mejorable.
def wordBetween(pStart,pEnd,phrase,include):
    char1=pStart[0]
    char2=pEnd[0]
    val1,val2=False,False
    finalWord=''
    
    for i, char in enumerate(phrase):
        if char1==char and val1==False:
            for j, letter in enumerate(pStart):
                if letter==phrase[i+j]: val1=True
                else: 
                    val1=False
                    break

        if val1: finalWord+=char

        if char2==char and val2==False and val1==True:
            for j, letter in enumerate(pEnd):
                if letter==phrase[i+j]: val2=True
                else: 
                    val2=False
                    break
        
        if val2: break

    finalWord=finalWord[len(pStart):]

    if include==True: finalWord=pStart+finalWord+pEnd

    return finalWord

#A partir de una lista de coordenadas XY y la ubicación de un archivo PDF busca
#todas las palabras que estén en esas coordenadas hoja por hoja y almacena todas
#esas palabras en un diccionario con la metadata de cada palabra y retorna el
#diccionario. 
def wordPDFdic (listCC,pdfAddress):
    file=fitz.open(pdfAddress)
    wordDic={}

    for i, page in enumerate(file.pages(), start=1):
        wordList=[]
        xy=[1,2]
        for word in page.get_text('words'):
            xy[0]=word[0]
            xy[1]=word[1]
            if xy in listCC: wordList.append(word[4])
        wordDic[i]=wordList

    return wordDic

    