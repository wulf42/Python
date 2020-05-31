from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

# pobieramy wszystkie elementy typu <a> gdzie przodkiem jest <H2> oraz elementem nadrzędnym element o
# klasie "geekcentral_leftcol"
xpath = '//*[@class="media-module ng-scope""]//h2//a'

# iterowanie przez odnalezione elementy i wyświetlenie nazw i wartości atrybutów
foundElements = page.xpath(xpath)
for element in foundElements :
   print(element.tag, element.keys())
   for name, value in sorted(element.items()):
       print('%s = %r' % (name, value))