from bs4 import BeautifulSoup
import requests
import pandas
import os

url="https://replit.com/@DanielLuevano1/DraftyUnsteadyGnudebugger#main.py"
for i in range(1):
    page1=requests.get(url)
    soup1=BeautifulSoup(page1.content,"html.parser")
    print(soup1)
