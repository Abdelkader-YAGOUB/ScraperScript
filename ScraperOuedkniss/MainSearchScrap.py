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

csv_columns = ['idProduct','Name','Price','Mark','RAM','CPU','Screen','DiscCapacity','State','Adress','Phone','URL']

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
        idProduct = pt.find('span', {'class' : 'annonce_numero'}).text
        print(idProduct)
        urlProduct = pt.find('a', {'class' : 'button button_details'})

        # link details 
        urlDetails = 'https://www.ouedkniss.com/'+urlProduct.get('href')
        d = requests.get(urlDetails , verify=True)
        soup2 = BeautifulSoup(d.content, "html.parser")
        ancher2 =soup2.find_all('div',{'id' : 'annonce'})
        for pt2 in ancher2:
            name = pt2.find('h1', {'itemprop' : 'name'}).text
            print(name)

            if pt2.find('span', {'itemprop' : 'price'}):
                price = pt2.find('span', {'itemprop' : 'price'}).text
                print(price)
            else:
                print(BeginRED + "None value" + EndRED)

            if pt2.find('p', {'id' : 'Marque'}):
                mark_p = pt2.find('p', {'id' : 'Marque'})
                mark_class = mark_p.find('span', {'class' : 'description_span'}).text
                print(mark_class)
            else:
                print(BeginRED + "None value" + EndRED)

            if pt2.find('p', {'id' : 'RAM'}):
                RAM_p = pt2.find('p', {'id' : 'RAM'})
                RAM_class = RAM_p.find('span', {'class' : 'description_span'}).text
                print(RAM_class)
            else:
                print(BeginRED + "None value" + EndRED)

            if pt2.find('p', {'id' : 'RAM'}):
                RAM_p = pt2.find('p', {'id' : 'RAM'})
                RAM_class = RAM_p.find('span', {'class' : 'description_span'}).text
                print(RAM_class)
            else:
                print(BeginRED + "None value" + EndRED)    

            if pt2.find('p', {'id' : 'Processeur'}):
                processeur_p = pt2.find('p', {'id' : 'Processeur'})
                processeur_class = processeur_p.find('span', {'class' : 'description_span'}).text
                print(processeur_class)
            else:
                print(BeginRED + "None value" + EndRED)
            
            if pt2.find('p', {'id' : 'Dimensions écran'}):
                dimensionScreen_p = pt2.find('p', {'id' : 'Dimensions écran'})
                dimensionScreen_class = dimensionScreen_p.find('span', {'class' : 'description_span'}).text
                print(dimensionScreen_class)
            else:
                print(BeginRED + "None value" + EndRED)

            if pt2.find('p', {'id' : 'Disque'}):
                disque_p = pt2.find('p', {'id' : 'Disque'})
                disque_class = disque_p.find('span', {'class' : 'description_span'}).text
                print(disque_class)
            else:
                print(BeginRED + "None value" + EndRED)

            if pt2.find('p', {'id' : 'Etat'}):
                state_p = pt2.find('p', {'id' : 'Etat'})
                state_class = state_p.find('span', {'class' : 'description_span'}).text
                print(state_class)
            else:
                print(BeginRED + "None value" + EndRED)

            if pt2.find('div', {'id' : 'Annonceur'}):
                adress_p = pt2.find('div', {'id' : 'Annonceur'})
                adress_class = adress_p.find('p', {'class' : 'Adresse'}).text
                print(adress_class)
            else:
                print(BeginRED + "None value" + EndRED)

            if pt2.find('div', {'id' : 'Annonceur'}):
                phone_p = pt2.find('div', {'id' : 'Annonceur'})
                phone_p1 = phone_p.find('p', {'id' : 'direct_call'})
                phone_class = phone_p1.find('a').text
                print(phone_class)
            else:
                print(BeginRED + "None value" + EndRED)


            # Add data to CSV file
            writer.writerow({'idProduct': idProduct,
                            'Name': name,
                            'Price': price,
                            'Mark': mark_class,
                            'RAM': RAM_class,
                            'CPU': processeur_class,
                            'Screen': dimensionScreen_class,
                            'DiscCapacity': disque_class,
                            'State': state_class,
                            'Adress': adress_class,
                            'Phone': phone_class,
                            'URL': urlDetails})
        print("--------------")

filecsv.close()
