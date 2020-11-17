
num_count = 0


while num_count != 100:
    
    num_count += 1
    if num_count % 3 == 0:
        print("fizz")

    if num_count % 5 == 0:
        print("buzz")

    if num_count % 3 == 0 and num_count % 5 == 0:
        print("fizzbuzz")
    if num_count % 3 != 0 and num_count % 5 != 0:
      print(num_count)
