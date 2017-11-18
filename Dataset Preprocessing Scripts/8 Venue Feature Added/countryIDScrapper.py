import urllib2
from bs4 import BeautifulSoup

dict = {}

ourCountryID = [1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,19,20,25,26,27,28,29,30,32,40,48,187,216]

for ourId in ourCountryID:
	myLinkHit = 'http://stats.espncricinfo.com/ci/engine/records/index.html?id={};type=team'.format(ourId)
	page = urllib2.urlopen(myLinkHit)

	soup = BeautifulSoup(page,'html.parser')
	ourText = soup.find('div', attrs = {'class':'icc-home'})
	
	countryName = ourText.contents[0].split("/")[1].strip()

	if countryName:
		dict[ourId] = countryName
		print(countryName,":FOUND")

print(dict)
