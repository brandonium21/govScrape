#import Dependancies
from urllib2 import *
import urllib2
import csv
import requests
from bs4 import BeautifulSoup

# retrieve form actions on page 
flags = ['navient', 'violate']
docType= ['8-K', '10-Q', '10-K']
doc = '8-K'
flagged = []

currentYear = ''
# date to stop given in format: YYYY-MM-DD
stopYear = '2016-09-14'

def keepScrape():
	count = 100
	try:
		iterationSearchString = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=' + doc + '&SIC=&State=&Country=&CIK=&owner=include&accno=&start=' + str(count) + '&count=100'
		searchString = 'https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=&type=' + doc + '&owner=include&count=100&action=getcurrent'
		response = urllib2.urlopen(searchString)
		
		soup = BeautifulSoup(response, "html.parser")
		
		while any(stopYear in s for s in soup.findAll('td')):
			response = urllib2.urlopen(iterationSearchString)
			for link in soup.find_all('a'):
				if flags[0] in (link.getText().encode('utf8').lower()): 
					flagged.append((link.getText(),link.get('href')))
			count += 100
			return currentYear
	except HTTPError, status:
		return status
	return # current Year

def save(): 
	return #saved as true false if not 

# loop though form action
while stopYear != currentYear:
	print flagged
	currentYear = keepScrape()


# check if string includes the string

# if includes check var save in array

# else keep looping

# stop when Done