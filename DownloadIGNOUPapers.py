#This file can be used to fetch PDF files from IGNOU to download the yearWise previous papers
import pandas as pd
from bs4 import BeautifulSoup
import requests as req
import re
yearUrl="https://webservices.ignou.ac.in/Pre-Question/"    #Actual URL for all year papers
allyearpage=req.get(yearUrl)
soup = BeautifulSoup(allyearpage.text,'html.parser')
yeartable=soup.find('table')                               #As there is a single table in the page we used find, otherwise we could have used findAll
yearlinks = yeartable.findAll('a')                         #Now finding the anchor tag
#'a', attrs={'href': re.compile("^http://")}):
for yearlink in yearlinks:
    print(str(yearlink))
    s=str(yearlink)
    l = s.split('"')[1::2];                               #this prints 2,4,6th elements[index wise odd]... ie. even elements
    yearExtractedLink=l[0]
    if 'http' not in yearExtractedLink:
        yearExtractedLink=yearUrl+yearExtractedLink


    print (yearExtractedLink)


def yearWisePapers(yearLink):

    return 'ss'
