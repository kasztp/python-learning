import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_links(link):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags


url = 'http://py4e-data.dr-chuck.net/known_by_Lucais.html'
count = int(input("Enter count: "))
position = int(input("Enter position: "))

for i in range(0, count):
    print('Retrieving: ', url)
    links = get_links(url)
    counter = 0
    for link in links:
        counter += 1
        url = link.get('href', None)
        if counter == position:
            break

print(url)

