from bs4 import BeautifulSoup
from urllib2 import *
import unicodedata
doc = '8-K'

searchString = 'https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=&type=' + doc + '&owner=include&count=100&action=getcurrent'
flagged = []
response = urlopen(searchString).read()
html = response
#print html
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all('a'):
	if 'discover' in link.getText().lower(): 
		flagged.append(link.get('href'))

#print flagged
#print len(flagged)
for i in soup.findAll('td'):
	if (i.getText().encode('utf8')) == '2016-09-16': 
		print i.getText()
#print table
#print (soup.findAll('table')[5].findAll('td'))

#print table.prettify()