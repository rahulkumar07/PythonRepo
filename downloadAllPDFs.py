#!/usr/bin/env python
# coding: utf-8

# In[9]:
#Download all pds from a URL

import pandas as pd
from bs4 import BeautifulSoup
import requests as req
import re
import os

dirname=['C:\\Users\\NRkPC\\Desktop\\ChatBot']

def main():
    yearUrl="customURL/"    #Actual URL for all year papers
    allyearpage=req.get(yearUrl)
    soup = BeautifulSoup(allyearpage.text,'lxml')
    allyearstable=soup.findAll('a')                               #As there is a single table in the page we used find, otherwise we could have used findAll
    #allyearlinks = allyearstable.findAll('a')
    for yearlink in allyearstable:
        #print(str(yearlink))
        s=str(yearlink)
        econrawURL=s.split('href')[1].split('"')[1]
        
        if 'http' not in econrawURL:
            econrawURL=yearUrl.rsplit('/',1)[0]+"/"+econrawURL
        print(str(econrawURL))
        if '.pdf' in econrawURL:
            downloadFiles(econrawURL)
        
def downloadFiles(url):
    print("URL from download:"+url)
    r = req.get(url)
    print("ss::"+url.rsplit('/',1)[1]+dirname[0])
    file= open(dirname[0]+"/"+url.rsplit('/',1)[1], 'wb')
    file.write(r.content)
    file.close()
    
    
if __name__ == '__main__':
    main()        


# In[ ]:




