#This file can be used to fetch data from moneycontrol.com give MF url as parameter to this file
import urllib3
import sys
import requests as rq
from bs4 import BeautifulSoup

mf_url=sys.argv[1]
print ('Fetching data from URL:',mf_url)
page=rq.get(mf_url)
soup = BeautifulSoup(page.text, 'html.parser')
rank_lst=soup.find_all(class_='bl_14')
rank_in_categ= str(rank_lst[0].contents[0]).replace('<b>','').replace('</b>','')
mf_category=str(rank_lst[1].contents[0]).replace('<b>','').replace('</b>','')
rank_str=rank_in_categ+' in '+mf_category
print (rank_str)
portFolio_lst=soup.find_all(class_='tblporhd')[2].find_all(class_='bl_13')
for portFolio_lst_itms in portFolio_lst:
    print (portFolio_lst_itms.contents[0])

