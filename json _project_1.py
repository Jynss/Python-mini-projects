import urllib.request, urllib.parse, urllib.error
import ssl
import json

#Dr. Chuck said ignore this
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



adress = input("Enter location: ")
print("Retrieving http:",adress)
pre_jason = urllib.request.urlopen(adress, context=ctx).read()
jason = pre_jason.decode()
info = json.loads(jason)
numbers = []

for line in info["comments"]:
 number = int(line["count"])
 numbers.append(number)

print("Retrieved", len(pre_jason) ,"characters")
print("Count: ", len(info["comments"]))
print("Sum:", sum(numbers))


