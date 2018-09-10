import bs4 as bs
import urllib.request
source = urllib.request.urlopen('http://python.org/').read()
soup = bs.BeautifulSoup(source,'lxml')
print(soup.title)
#for para in soup.find_all('p'):
#	print(para.text)
#print(soup.get_text())
for url in soup.find_all('a'):
    print(url.get('href'))
