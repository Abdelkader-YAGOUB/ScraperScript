import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import json
import csv
import os
import re
from beautifultable import BeautifulTable

# Color for text
BeginRED = '\033[91m'
EndRED = '\033[0m'

BeginBLUE = '\033[94m'
EndBLUE = '\033[0m'

# URL webscrape manga web site
url = 'http://www.mangapanda.com'
pathMangaFolder = "./ScraperManaga/"

# Popular Manga list
r = requests.get(url, verify=True)
soup = BeautifulSoup(r.content, "html.parser")

table = BeautifulTable()
table.columns.header = [BeginBLUE +"MangaName"+ EndBLUE, BeginBLUE +"Link"+ EndBLUE]
for link in soup.find_all('a',{'class' : 'popularitemcaption'}):
    NameManga = link.text
    LinkManga = link.get('href')
    table.rows.append([NameManga, url+LinkManga])

print(BeginRED + "# Popular Manga # \n" + EndRED)
table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
print(table)
inputMangaName = input("Choose one # (Just write the name of the manga) : ") # Example = One Piece

urlMangaData = "" 
i = 0
while i < 40:
    if table.rows[i][0] == inputMangaName :
        #print(table.rows[i][0])
        #print(table.rows[i][1])
        urlMangaData = table.rows[i][1]
        break
    else:
        i += 1

print(BeginBLUE + "" + urlMangaData + ""+ EndBLUE)

# Range chapter we want to download 
print("Range chapters you want to download \n")
inputChapterDownloadFrom = int(input("From chapter : ")) # Example chapter : 985
inputChapterDownloadTo = int(input("To chapter : ")) # Example chapter : 988

for chap in range(inputChapterDownloadFrom, inputChapterDownloadTo):
    print("Chaprer :", chap)

    # Create folder
    os.makedirs(pathMangaFolder+'/'+'Manga-'+inputMangaName+'/Chapter'+str(chap))
    chapterPage = 1
    
    # Get link while exist = True
    while requests.get(urlMangaData + '/'+ str(chap) + '/'+ str(chapterPage)):
        urlChapter = urlMangaData + '/'+ str(chap) + '/'+ str(chapterPage)
        print(urlChapter)
        r2 = requests.get(urlChapter)
        soup2 = BeautifulSoup(r2.content, "html.parser")

        # Find url image
        for ancher2 in soup2.find_all('img',{'id':'img'}):
            urlImg = ancher2.get('src')
            print(urlImg)
            # download image from url
            response = requests.get(urlImg)
            file = open(pathMangaFolder+'/'+'Manga-'+inputMangaName+'/Chapter'+str(chap)+'/'+str(chapterPage)+".jpg", "wb")
            file.write(response.content)
            file.close()
        chapterPage += 1
