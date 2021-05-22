from bs4 import BeautifulSoup
import requests
import pandas
import os
from c import creador
from exclel import excel
from recolect_table import table
##Creacion de las carpetas para el vaciado de informacioon
def creadortxt():
    lista=["José Juan Macías","Uriel Antuna","Isaac Brizuela","Jesus Angulo","Jesus Sánchez","Campeonismo","Vergara y el renacer","La Epoca Reciente","Fechas partidos","Hora partidos","Marcador final","Liga"]
    n=1
    for i in lista:
        b=i
#    for i in range(5):
        archivo=open(b+".txt","w")


#Lecturadel archivo que contiene los links
archivo=open("urls.txt","r")
links=archivo.readlines()
url1=links[0]
url2=links[1]
url3=links[2]
url4=links[3]
url5=links[4]
url6=links[5]
url7=links[6]
#Peticiones a cada uno de los links
page1=requests.get(url1)
page2=requests.get(url2)
page3=requests.get(url3)
page4=requests.get(url4)
page5=requests.get(url5)
page6=requests.get(url6)
page7=requests.get(url7)
print(page1,page2,page3,page4,page5,page6,page7)
#print(url6)
archivo.close()
#llamdas al servidor para recoleccion de html
soup1=BeautifulSoup(page1.content,"html.parser")
origen=soup1.find_all("div",class_="text-wrapper base-content")
##
soup2=BeautifulSoup(page2.content,"html.parser")
cincojugadores=soup2.find_all("h2")
##
soup3=BeautifulSoup(page3.content,"html.parser")
Macias=soup3.find_all("p",style="text-align: justify;")
##
soup4=BeautifulSoup(page4.content,"html.parser")
uriel=soup4.find_all("p")

##
soup5=BeautifulSoup(page5.content,"html.parser")
isaac=soup5.find_all("p")
##
soup6=BeautifulSoup(page6.content,"html.parser")
JesusA=soup6.find_all("p",style="text-align: justify;")
##
soup7=BeautifulSoup(page7.content,"html.parser")
JesusSA=soup7.find_all("p",style="text-align: justify;")
##

##Peticiones de los archivos que necesitan extraer solo algunas etiquetas <p> del HTML
c=3
j=[]
for i in range(4):
    u=uriel[c].getText()
    j.append(u)
    c+=1
#print(j)
##
t=[]
x=3
for i in range(4):
    c=isaac[x].getText()
    t.append(c)
    x+=1
#print(t)
##
c=0
for i in range(1):
    o1=origen[c].getText()
    c+=1
#    print(o1)
##
c=1
for i in range(1):
    s3=[]
    o2=origen[c].getText()
    s3.append(o2)
    c+=1
#    print(o2)
##
c=2
for i in range(1):
    s=[]
    o3=origen[c].getText()
    s.append(o3)
    c+=1
##
c=3
for i in range(1):
    s2=[]
    o4=origen[c].getText()
    s2.append(o4)
    c+=1

##
#for i in JesusSA:
#    print(i.text+"\n")
#print(origen)
##
##Creacion de archivo con la historia delorigen de chivas
archivo=open("El origen.txt","w")
archivo.write(o1+"\n")
archivo.close()
##
##
##rellenar con informacion los txt
def Archivos():
    archivo=open("José Juan Macías.txt","w")
    for i in Macias:
        archivo.write(i.text+"\n")
    archivo.close()
    archivo=open("Jesus Angulo.txt","w")
    for i in JesusA:
        archivo.write(i.text+"\n")
    archivo.close()
    archivo=open("Jesus Sánchez.txt","w")
    for i in JesusSA:
        archivo.write(i.text+"\n")
    archivo.close()
    archivo=open("nombres jugadores.txt","w")
    for i in cincojugadores:
       archivo.write(i.text+"\n")
    archivo.close()
    archivo=open("Isaac Brizuela.txt","w")
    for i in t:
        archivo.write(i+"\n")
    archivo.close()
    archivo=open("Uriel Antuna.txt","w")
    for i in j:
        archivo.write(i+"\n")
    archivo.close()
    archivo=open("La Epoca Reciente.txt","w")
    for i in s2:
        archivo.write(i)
    archivo.close()
    archivo=open("Campeonismo.txt","w")
    for i in s3:
        archivo.write(i)
    archivo.close()
##
    archivo=open("Vergara y el renacer.txt","w")
    for i in s:
        archivo.write(i)
    archivo.close()
##
if __name__=="__main__":
    creadortxt()
    Archivos()
    table()
    excel()
    creador()
