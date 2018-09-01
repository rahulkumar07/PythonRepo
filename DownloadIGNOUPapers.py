#This file can be used to fetch PDF files from IGNOU to download the yearWise previous papers
import pandas as pd
from bs4 import BeautifulSoup
import requests as req
import re
import os

dirname=[''] #defining a global variable for the directory in which files are going to be saved

def main():
    yearUrl="https://webservices.ignou.ac.in/Pre-Question/"    #Actual URL for all year papers
    allyearpage=req.get(yearUrl)
    soup = BeautifulSoup(allyearpage.text,'lxml')
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
        dirname[0]=yearExtractedLink.rsplit("/",1)[1].split(".")[0]
        if(not os.path.isdir(dirname[0])):
            os.mkdir(dirname[0])
        #else:
        #    print("already exists:"+dirname[0])
        yearWisePapers(yearLink=yearExtractedLink)

def yearWisePapers(yearLink):

    try:
        if not ('2005' in yearLink or '2006' in yearLink or '2007' in yearLink):
            print ("Inside yearWisePapers for "+yearLink)
            yearpage=req.get(yearLink)
            soup = BeautifulSoup(yearpage.text,'html.parser')
            yeartable=soup.findAll('table')
            course_rows = yeartable[0].findAll('tr')
            for course_row in course_rows:
                #print (course_row)
                s=str(course_row)
                if 'Arts in Economics' in s:
                    econrawURL=s.split('href')[1].split('"')[1]
                    if 'http' not in econrawURL:
                        econrawURL=yearLink.rsplit('/',1)[0]+"/"+econrawURL

                    getPDFURLfromURL(econrawURL,"MEC")


        return 'ss'
    except Exception as e:
        print ("Exception occured while opening the connection, now moving to next"+str(e))
        return str(e)

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
                #print (course_row)
        return 'ss'
    except Exception as e:
        return str(e)

def downloadFiles(url):
    print("URL from download:"+url)
    r = req.get(url)
    print("ss::"+url.rsplit('/',1)[1]+dirname[0])
    file= open(dirname[0]+"/"+url.rsplit('/',1)[1], 'wb')
    file.write(r.content)
    file.close()





if __name__ == '__main__':
    main()
