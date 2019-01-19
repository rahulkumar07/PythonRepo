#This file can be used to fetch PDF files from IGNOU to download the yearWise previous papers
import pandas as pd
from bs4 import BeautifulSoup
import requests as req
import re
import os

dirname=['']
siteUrl="http://egyankosh.ac.in"

def main():
    courseUrl="http://egyankosh.ac.in/handle/123456789/5656"    #Actual URL for all course links
    allcoursess=getNextUrlLst(courseUrl,'div','list-group')                         #Now finding the anchor tag

    #'a', attrs={'href': re.compile("^http://")}):
    i=0
    for courses in allcoursess:
        print(str(courses)+str(i))
        i=i+1;
        s=str(courses)
        l = s.split('"')[1::2];                               #this prints 2,4,6th elements[index wise odd]... ie. even elements
        yearExtractedLink=l[0]
        if 'http' not in yearExtractedLink:
            yearExtractedLink=siteUrl+yearExtractedLink
        dirname[0]=((s.split('>'))[1].split('<')[0]).strip()
        print('dirname'+dirname[0])
        if(not os.path.isdir(dirname[0])):
            os.mkdir(dirname[0])
        #else:
        #    print("already exists:"+dirname[0])
        courseWiseBlockLinks(courses=yearExtractedLink,dirname=dirname[0])

def courseWiseBlockLinks(courses,dirname):
    try:
        if (courses):
            print ("Inside yearWisePapers for "+courses)
            course_rows=getNextUrlLst(courses,'div','list-group')
            #print(course_rows)
            s=str(course_rows)
            l = s.split('"')[1::2];                               #this prints 2,4,6th elements[index wise odd]... ie. even elements

            #course_rows=course_rows.findAll('a')
            for course_row in l:
                if 'http' not in course_row:
                    yearExtractedLink=siteUrl+course_row
                    print('BLOCK LINK::'+yearExtractedLink)
                    finalPDFlstURL=getNextUrlLst(yearExtractedLink,'table','table')
                    print('finalPDFlstURL')
                    print(finalPDFlstURL)
                    s=str(finalPDFlstURL)
                    unit_row_list = s.split('"')[1::2];
                    for unit_row in unit_row_list:
                        if 'http' not in unit_row:
                            unitURL=siteUrl+unit_row
                            print('unitURL:'+unitURL)
                            unitPDFLinkList=getNextUrlLst(unitURL,'table','table panel-body')
                            print('unitPDFLinkList')
                            print(unitPDFLinkList)
                            s=str(unitPDFLinkList)
                            unit_pdf_partial_link_list = s.split('"')[1::2];
                            for unit_pdf_partial_link in unit_pdf_partial_link_list:
                                unit_pdf_link=siteUrl+unit_pdf_partial_link
                                print('unit_pdf_link'+unit_pdf_link)
                                if 'pdf' in unit_pdf_link and 'pdf.jpg' not in unit_pdf_link:
                                    downloadFiles(unit_pdf_link,dirname)

                    #getPDFURLfromURL(econrawURL,"MEC")


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
                print("ddd:"+econrawURL)

                #print (course_row)
        return 'ss'
    except Exception as e:
        return str(e)

def downloadFiles(url,dirname):
    print("URL from download:"+url)
    r = req.get(url)
    #print("ss::"+url.rsplit('/',1)[1]+dirname[0])
    file= open(dirname+"/"+url.rsplit('/',1)[1], 'wb')
    file.write(r.content)
    file.close()

def getNextUrlLst(url,elementname,className):
    courseUrlReq=req.get(url)
    soup = BeautifulSoup(courseUrlReq.text,'lxml')
    #print(soup)
    listofCourses=soup.findAll(elementname, attrs={'class':className})
    print("listofCourses")
    #print(listofCourses)                               #As there is a single table in the page we used find, otherwise we could have used findAll
    returnobj=''
    if(listofCourses):
        returnobj=listofCourses[0].findAll('a')
    return returnobj                        #Now finding the anchor tag





if __name__ == '__main__':
    main()
