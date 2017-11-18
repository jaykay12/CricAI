import urllib2
from bs4 import BeautifulSoup
import pandas as pd

ourCountryId = {1: u'England', 2: u'Australia', 3: u'South Africa', 4: u'West Indies', 5: u'New Zealand', 6: u'India', 7: u'Pakistan', 8: u'Sri Lanka', 
9: u'Zimbabwe', 11: u'United States of America', 12: u'Bermuda', 14: u'East (and Central) Africa', 15: u'Netherlands', 16: u'Malaysia', 
17: u'Canada', 19: u'Hong Kong', 20: u'Papua New Guinea', 25: u'Bangladesh', 26: u'Kenya', 27: u'United Arab Emirates', 28: u'Namibia', 
29: u'Ireland', 30: u'Scotland', 32: u'Nepal', 40: u'Afghanistan', 48: u'Zambia', 187: u'Qatar', 216: u'Vanuatu'}

venues = pd.DataFrame(columns = ['Ground','Host_Country'])

oldEnum = 0
for myID in ourCountryId.keys():
#for myID in [1,2,6]:
	myLinkHit = 'http://www.espncricinfo.com/ci/content/ground/city.html?country={}'.format(myID)

	page = urllib2.urlopen(myLinkHit)
	soup = BeautifulSoup(page, 'html.parser')

	print "Got Venues in:", ourCountryId[myID]

	for i,li in enumerate(soup.findAll('li')):
		venues.loc[i+oldEnum] = [li.contents[0], ourCountryId[myID]]

	oldEnum = oldEnum + i + 1

venues.to_csv('Venues.csv',index=False)