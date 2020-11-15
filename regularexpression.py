import re
trial = open('samplew2')
numbers = []
for line in trial:
  number = re.findall('[0-9]+',line)
  for digit in number:
    digit = int(digit)
    numbers.append(digit)

#print(numbers)

print(sum(numbers))


