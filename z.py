import bs4 as bs
import urllib.request
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')
print(soup.title)

for para in soup.find_all('p'):
	print(para.text)
print(soup.get_text())
for url in soup.find_all('a'):
   print(url.get('href'))
nav=soup.nav
print(nav)

 
for div in soup.find_all('div', class_='body'):
    print(div.text)
    
table=soup.find('table')
table_row=table.find_all('tr')

for tr in table_row:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)
