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
            