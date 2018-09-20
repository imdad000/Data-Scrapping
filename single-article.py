from bs4 import BeautifulSoup
import requests
import csv
import re, os

base_url = 'https://web.archive.org/web/20180103221846/http://www.htcampus.com/article/uceed-previous-years-exam-analysis/'
headers = {'User-agent': 'Mozilla/5.0'}
webpage = requests.get(base_url, headers=headers )
soup = BeautifulSoup(webpage.content, "html.parser")
t=soup.find('div', class_='col-lg-3 col-md-3 col-sm-3').decompose()
t=soup.find('div', class_='comments-wrap').decompose()
t=soup.find('div', class_='like-on-us').decompose()
t=soup.find('div', class_='content-wrap clearfix').decompose()
t=soup.find('ul', class_='related_articles_list').decompose()
t=soup.find('div', class_='article-tags').decompose()
t=soup.find('div', class_='green-border-wrap').decompose()
t=soup.find('div', class_='article-list').decompose()
for x in soup.find_all('a'):
    t=x.decompose()


for x in soup.find_all('div', class_='rec-article-box'):
    t=x.decompose()

t=soup.find('div',class_='article-content')
print(t)
	
   
    












    
	
                     
                     



                     
  
