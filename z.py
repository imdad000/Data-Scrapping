import bs4 as bs
import urllib.request
source = urllib.request.urlopen('http://python.org/').read()
soup = bs.BeautifulSoup(source,'lxml')
print(soup.title)
print(soup.find_all('p'))
