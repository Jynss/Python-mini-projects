name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
count = dict()
handles = []

for lines in handle:
    if not lines.startswith("From "):
        continue

    lines = lines.split()
    lines = lines[1]
    
    count[lines] = count.get(lines, 0) + 1


email = None
times_called = None
for key,value in count.items():
  if times_called is None or value > times_called:
    email = key
    times_called = value 


#print(count)
#print("\n"*2)
#print(handles)
#print("\n"*2)


print(email,times_called)