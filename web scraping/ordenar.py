import os
import sys
import shutil
import time
from random import randint
### Aqui colocas tu carpeta que quieres ordenar
ruta_Escritorio = ("C:/Users/mcdan/OneDrive/Escritorio/prueba/")
ext_texto=[".txt"]
ext_python=[".py"]
ext_Excel=[".xlsx"]



def ordenar(archivo,ext):
    for i in ext_texto:
        if ext==i:
            shutil.move(ruta_Escritorio + archivo,ruta_Escritorio + "Base De datos")
    for i in ext_python:
        if ext==i:
            shutil.move(ruta_Escritorio + archivo,ruta_Escritorio + "Python")
    for i in ext_Excel:
        if ext==i:
            shutil.move(ruta_Escritorio + archivo,ruta_Escritorio + "excel")
def main():
    for archivo in os.listdir(ruta_Escritorio):
        nombre_archivo,ext=os.path.splitext(archivo)
        ordenar(archivo,ext)

main()
