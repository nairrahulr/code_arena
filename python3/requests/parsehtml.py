#This will not run on online IDE
import requests
from bs4 import BeautifulSoup
 
URL = "http://www.google.com"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())