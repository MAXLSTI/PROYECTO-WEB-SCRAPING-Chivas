from bs4 import BeautifulSoup
import requests
import pandas
import os
import re
def table():
    url="https://www.goal.com/es-mx/noticias/chivas-cuando-juega-calendario-partidos/1q9szu2xjwb0r1cd1ef23jii4x"
    page7=requests.get(url)
    print("La peticion fue codigo ",page7)
    soup1=BeautifulSoup(page7.content,"html.parser")
    origen=soup1.find_all("td",style="text-align: center;")
    origen2=soup1.find_all("a")
##
    archivo=open("table.txt","w")
    for i in origen:
        archivo.write(i.text)
    archivo.close()
    archivo=open("table.txt","r")
    list=["([A-Z]+\s)+\C\w+\Ó\w","\d\d/\d\d/\d{4}","\d\d:\d\d","\s[A-Z]+[a-z]+(\s\d\-\d)\s[A-Z]+[a-z]+","[A-Z]+[a-z]+\s[A-Z]{2}"]
    patron=list[1]
    patron2=list[2]
    patron3=list[3]
    patron4=list[4]
    text=archivo.read()
    x=re.findall(patron,text)
    x2=re.findall(patron2,text)
    x3=re.findall(patron3,text)
    x4=re.findall(patron4,text)
    a=[]
    for i in x:
        a.append(i)
    a2=[]
    for i in x2:
        a2.append(i)
#a3=[]
#for i in x3:
#    a3.append(i)
#print(a3)
    a4=[]
    for i in x4:
        a4.append(i)
    a5=[]
    for i in origen2:
        a5.append(i.text)
    archivo=open("Fechas partidos.txt","w")
    for i in a:
        archivo.write(i+"\n")
    archivo.close()
    archivo=open("Hora partidos.txt","w")
    for i in a2:
        archivo.write(i+"\n")
    archivo.close()
    archivo=open("Liga.txt","w")
    for i in a4:
        archivo.write(i+"\n")
    archivo.close()
    archivo=open("Marcador final.txt","w")
    for i in a5[7:24]:
        archivo.write(i+"\n")
    archivo.close()
