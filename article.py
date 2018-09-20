from bs4 import BeautifulSoup
import requests
import csv
import re, os

ITI_INDEX=0
mba_clg=[]
base_url = 'https://web.archive.org/web/20180221031120/http://www.htcampus.com:80/article/hospitality-management-category/'
headers = {'User-agent': 'Mozilla/5.0'}
webpage = requests.get(base_url, headers=headers )
soup = BeautifulSoup(webpage.content, "html.parser")
page_count=1
arr=[]
i=0
stores_url = []
DMP_PATH = 'mba-category'

if not os.path.exists(DMP_PATH):
    os.mkdir(DMP_PATH)

with open('Article.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([ 'P_No', 'Title', 'URL','File_Name', 'Status-code' ])
page_url=base_url
while True:
    print(page_url)
    webpage = requests.get(page_url, headers=headers )
    page_url = base_url+'?page='+str(page_count)
    print(webpage.status_code)
    soup = BeautifulSoup(webpage.content, "html.parser")
    h2=soup.find_all('h2',class_='media-heading category-head border-0')
    with open('Article.csv', 'a') as f:
        writer = csv.writer(f)
        for x in h2 :
            title = ""
            title=x.string
            url = x.find('a')['href']
            url='https://web.archive.org'+url
            webpage1 = requests.get(url)
            status_code=webpage1.status_code
            with open("hospitility-article"+str(i),'wb') as f: 
                f.write(webpage1.content) 
            stores_url.append(x.find('a')['href'])
            print(webpage1.content)
            file_name="hospitility-article"+str(i)
            writer.writerow([page_count, title, url,file_name,status_code])
            i=i+1
    if not len(h2):
        break
    page_count=page_count+1
	
   
    












    
	
                     
                     



                     
  
