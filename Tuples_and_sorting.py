name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
times = dict()
sorted_times = []

for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    line = line[5]
    time = line.split(":")
    hour = time[0]
    times[hour] = times.get(hour, 0) + 1
    #print(time)

#print(times)

for k, v in times.items():
    for_sort = k,v 
    sorted_times.append(for_sort)

sorted_times = sorted(sorted_times )

#print(sorted_times)
#print("\n")
for time,num in sorted_times:
  print(time,num)