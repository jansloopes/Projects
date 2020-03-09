# import libraries
import requests

from bs4 import BeautifulSoup

quote_page = 'https://www.studeersnel.nl/nl/document/hogeschool-leiden/inleiding-organisatiekunde/samenvattingen/itorg-aantekeningen-en-kahoot-antwoorden/4187917/view'
page = requests.get(quote_page)
print(page)
