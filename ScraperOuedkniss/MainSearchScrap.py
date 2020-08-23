import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
import os
import re

# Color for text
BeginRED = '\033[91m'
EndRED = '\033[0m'

# remove a file if exists
fileExistPath = './ScraperOuedkniss/OuedknissLaptopData.csv'
if os.path.exists(fileExistPath):
    os.remove(fileExistPath)

# Generate csv file
filecsv = open('./ScraperOuedkniss/OuedknissLaptopData.csv', 'w',encoding='utf8')
inputMaRc = input("Enter laptop mark : ")  # Input mark -- toshiba
# URL webscrape 
url = 'https://www.ouedkniss.com/annonces/index.php?c=informatique&sc=ordinateur-portable&photo=1&marque='+ inputMaRc +'&p='

csv_columns = ['idProduct','Name','Price','Mark','RAM','CPU','Graphic','Screen','DiscCapacity','State','Adress','Phone','URL']

# range(1) -> 1 page
for page in range(1):
    print("[", page, "]")
    r = requests.get(url + str(page) , verify=True)
    soup = BeautifulSoup(r.content, "html.parser")
    ancher=soup.find_all('div',{'class' : 'annonce annonce_store'})
    writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
    i=0
    writer.writeheader()
    for pt in ancher:
        idProduct = pt.find('span', {'class' : 'annonce_numero'})
        urlProduct = pt.find('a', {'class' : 'button button_details'})

        # link details 
        urlDetails = 'https://www.ouedkniss.com/'+urlProduct.get('href')
        d = requests.get(urlDetails , verify=True)
        soup2 = BeautifulSoup(d.content, "html.parser")
        ancher2 =soup2.find_all('div',{'id' : 'annonce'})
        for pt2 in ancher2:
            name = pt2.find('h1', {'itemprop' : 'name'})
            price = pt2.find('span', {'itemprop' : 'price'})
            print(name.text)
            if price is not None:
                print(BeginRED + "" + price.text + "" + EndRED)
            mark_p = pt2.find('p', {'id' : 'Marque'})
            mark_class = mark_p.find('span', {'class' : 'description_span'})
            print(mark_class.text)

            try:
                RAM_p = pt2.find('p', {'id' : 'RAM'})
                RAM_class = RAM_p.find('span', {'class' : 'description_span'})
                if RAM_class is not None:
                    print(RAM_class.text)
            except:
                RAM_class = "None value"
            
            try:
                processeur_p = pt2.find('p', {'id' : 'Processeur'})
                processeur_class = processeur_p.find('span', {'class' : 'description_span'})
                if processeur_class is not None:
                    print(processeur_class.text)
            except:
                processeur_class = "None value"

            try:
                dimensionScreen_p = pt2.find('p', {'id' : 'Dimensions écran'})
                dimensionScreen_class = dimensionScreen_p.find('span', {'class' : 'description_span'})
                if dimensionScreen_class is not None:
                    print(dimensionScreen_class.text)
            except:
                dimensionScreen_class = "None value"

            try:
                disque_p = pt2.find('p', {'id' : 'Disque'})
                disque_class = disque_p.find('span', {'class' : 'description_span'})
                if disque_class is not None:
                    print(disque_class.text)
            except:
                disque_class = "None value"

            try:
                graphic = pt2.find('p', {'class' : 'description_span'})
                if graphic is not None:
                    print(graphic.text)
            except:
                graphic = "None value"

            try:
                state_p = pt2.find('p', {'id' : 'Etat'})
                state_class = state_p.find('span', {'class' : 'description_span'})
                if state_class is not None:
                    print(state_class.text)
            except:
                state_class = "None value"

            try:
                adress_p = pt2.find('div', {'id' : 'Annonceur'})
                adress_class = adress_p.find('p', {'class' : 'Adresse'})
                if adress_class is not None:
                    print(adress_class.text)
            except:
                adress_class = "None value"

            try:
                phone_p = pt2.find('div', {'id' : 'Annonceur'})
                phone_p1 = phone_p.find('p', {'id' : 'direct_call'})
                phone_class = phone_p1.find('a')
                if phone_class is not None:
                    print(phone_class.text)
            except:
                phone_class = "None value"

            # Add data to CSV file
            writer.writerow({'idProduct': idProduct.text,
                            'Name': name.text,
                            'Price': price.text,
                            'Mark': mark_class.text,
                            'RAM': RAM_class.text,
                            'CPU': processeur_class.text,
                            'Graphic': graphic,
                            'Screen': dimensionScreen_class.text,
                            'DiscCapacity': disque_class.text,
                            'State': state_class.text,
                            'Adress': adress_class.text,
                            'Phone': phone_class.text,
                            'URL': urlDetails})
        print("--------------")

filecsv.close()
