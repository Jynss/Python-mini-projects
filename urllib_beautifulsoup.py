import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


run_times = 0 
url = input('Enter - ')
count = int(input("Enter count: "))
position = int(input("Enter position: "))

#if run_times == 0:
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#tags = soup('a')


# Retrieve all of the anchor tags

#new_url = None

for x in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        if run_times != position:
            #print(tag.get('href', None))
            run_times += 1
            url = tag.get('href', None)
    run_times = 0
    print("Retrieving: ",url)
    