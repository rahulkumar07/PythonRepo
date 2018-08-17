#This file can be used to fetch PDF files from IGNOU to download the yearWise previous papers
import pandas as pd
from bs4 import BeautifulSoup
import requests as req
import re

def yearWisePapers(yearLink):
    print ("Inside yearWisePapers for "+yearLink)
    yearpage=req.get(yearLink)
    soup = BeautifulSoup(yearpage.text,'html.parser')
    yeartable=soup.findAll('table')
    course_rows = yeartable[0].findAll('tr')
    for course_row in course_rows:
        #print (course_row)
        s=str(course_row)
        if 'Master of Arts in Economics' in s:
            econrawURL=s.split('href')[1].split('"')[1]
            if 'http' not in econrawURL:
                econrawURL=yearLink.rsplit('/',1)[0]+"/"+econrawURL
            print(econrawURL)
            #print (course_row)
    return 'ss'



yearUrl="https://webservices.ignou.ac.in/Pre-Question/"    #Actual URL for all year papers
allyearpage=req.get(yearUrl)
soup = BeautifulSoup(allyearpage.text,'html.parser')
allyearstable=soup.find('table')                               #As there is a single table in the page we used find, otherwise we could have used findAll
allyearlinks = allyearstable.findAll('a')                         #Now finding the anchor tag
#'a', attrs={'href': re.compile("^http://")}):
for yearlink in allyearlinks:
    #print(str(yearlink))
    s=str(yearlink)
    l = s.split('"')[1::2];                               #this prints 2,4,6th elements[index wise odd]... ie. even elements
    yearExtractedLink=l[0]
    if 'http' not in yearExtractedLink:
        yearExtractedLink=yearUrl+yearExtractedLink
        yearWisePapers(yearLink=yearExtractedLink)

    print (yearExtractedLink)

