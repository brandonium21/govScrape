#import Dependancies
from urllib2 import *
import urllib2
import csv
import requests
from bs4 import BeautifulSoup
import csv
import sys
from itertools import groupby as g
import operator

# retrieve form actions on page 
flags = ['world', 'violate']
docType= ['8-K', '10-Q', '10-K']
doc = '8-K'
flagged = []

currentYear = ''
# date to stop given in format: YYYY-MM-DD
stopYear = '2016-09-16'



def most_common(L):
  return max(g(sorted(L)), key=lambda(x, v):(len(list(v)),-L.index(x)))[0]

def keepScrape():
	count = 100
	try:
		iterationSearchString = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&datea=&dateb=&company=&type=' + doc + '&SIC=&State=&Country=&CIK=&owner=include&accno=&start=' + str(count) + '&count=100'
		searchString = 'https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=&type=' + doc + '&owner=include&count=100&action=getcurrent'
		response = urllib2.urlopen(searchString)
		
		soup = BeautifulSoup(response, "html.parser")
		
		while any(stopYear not in s.getText() for s in soup.findAll('td')):
			response = urllib2.urlopen(iterationSearchString)
			for link in soup.find_all('a'):
				if flags[0] in (link.getText().encode('utf8').lower()): 
					flagged.append((link.getText(),link.get('href')))
					print 'current date being checked: ' + str(most_common(soup.findAll('td')))
					print 'Files Flagged : ' + str(len(flagged))
					print  'Files checked : ' + str(count)
					save()
				else:
					print 'None Found'
					print 'Files Flagged : ' + str(len(flagged))
					print  'Files checked : ' + str(count)
			count += 100
		
		return currentYear
	except HTTPError, status:
		return status


def save():
	f = open('results.csv', 'wt')
	try:
		writer = csv.writer(f)
		writer.writerow(('Description', 'link'))
		for titleHref in flagged:
			writer.writerow(titleHref)
	finally:
		f.close()
	print 'results saved to results.txt'
	print open('results.csv', 'rt').read()

keepScrape()

# check if string includes the string

# if includes check var save in array

# else keep looping

# stop when Done