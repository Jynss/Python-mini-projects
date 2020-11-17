print("Enter 5 numbers:")
number=int(input())
number_list= []
even_count = 0
odd_count = 0
number_limit=5

while number_limit !=0:
  number_list.append(number)
  number_limit= number_limit -1 
  if number_limit <= 5 and number_limit>0:
   number=int(input())
for num in number_list:
  if num % 2 == 0:
   even_count = even_count + 1
  
  else:
   odd_count = odd_count + 1

if number_limit ==0:
 print("There were" , even_count , "even numbers and" , odd_count, "odd numbers")


