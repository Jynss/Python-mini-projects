largest = None
smallest = None
while True:
    num = input()
    try:
        num=int(num)
    except:
        print("Invalid input")
        continue

    if num == "done" :
         break
    

print("Maximum", largest)
print("Minimum", smallest)