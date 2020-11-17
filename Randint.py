import random
guess=int(input("Guess a number from 1 - 100 "))


x=random.randint(1,100)
print (x)

if guess == x:
  print("You are correct")

else:
  print("I'm sorry you are wrong")
