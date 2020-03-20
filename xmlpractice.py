import urllib.request, urllib.error
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_392597.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

numbers = re.findall('\\b\\d+\\b', data.decode())
i = 0
for number in numbers:
    numbers[i] = int(number)
    i += 1
print('Sum: ', sum(numbers)-9)

