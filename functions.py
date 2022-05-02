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
