import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    print("Retrieving ",address)

    #opening file
    xml_file = urllib.request.urlopen(address, context=ctx).read()
    print("Retrieved: ", len(xml_file), "characters")
    #retrieving Lines of xml?????
    data = ET.fromstring(xml_file)
    counts = data.findall("comments/comment")

    counts_list = []
    for number in counts:
      actual_number =int(number.find("count").text)
      #print(actual_number)
      counts_list.append(actual_number)
   
    #for line in data.findall('.//count'):
     # print (data.text)
    print("Count: ", len(counts_list))
    print("Sum: ", sum(counts_list))
    break

  
    
    