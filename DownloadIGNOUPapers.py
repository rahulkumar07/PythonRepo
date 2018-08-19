#This file can be used to fetch PDF files from IGNOU to download the yearWise previous papers
import pandas as pd
from bs4 import BeautifulSoup
import requests as req
import re

def yearWisePapers(yearLink):
    print ("Inside yearWisePapers for "+yearLink)
    try:
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

                getPDFURLfromURL(econrawURL,"MEC")


        return 'ss'
    except Exception as e:
        print ("Exception occured while opening the connection, now moving to next")
        return str(e)

def downloadFiles(url):
    print("URL from download:"+url)
    r = req.get(url)
    print("ss::"+url.rsplit('/',1)[1])
    file= open(url.rsplit('/',1)[1], 'wb')
    file.write(r.content)
    file.close()


def getPDFURLfromURL(url,searchString):
    print ("Inside getPDFfromURL for "+url)
    try:
        pdfPage=req.get(url)
        soup = BeautifulSoup(pdfPage.text,'html.parser')
        yeartable=soup.findAll('table')
        course_rows = yeartable[0].findAll('tr')
        for course_row in course_rows:
            #print (course_row)
            s=str(course_row)
            if 'MEC' in s:
                econrawURL=s.split('href')[1].split('"')[1]
                if 'http' not in econrawURL:
                    econrawURL=url.rsplit('/',1)[0]+"/"+econrawURL

                downloadFiles(econrawURL)
                print("ddd:"+econrawURL)

                #print (course_row)
        return 'ss'
    except Exception as e:
        return str(e)

yearUrl="https://webservices.ignou.ac.in/Pre-Question/"    #Actual URL for all year papers
allyearpage=req.get(yearUrl)
soup = BeautifulSoup(allyearpage.text,'lxml')                   # earlier it was html.parser which didn't parse all.
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

