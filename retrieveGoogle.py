import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("https://spreadsheets.google.com/pub?key=0AujzeBNXnyI-dDNBRFJZaTZyRnZnMzdnQlFzSkRsd2c&hl=en&output=html")

soup = BeautifulSoup(page)
ted = soup.findAll('td',{ 'class' : 's1'})
for td in ted:
  print td.string
