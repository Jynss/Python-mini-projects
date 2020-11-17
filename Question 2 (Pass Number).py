print("Guess Pass Number")
pass_number = 484
guess = int(input())
guess_chances = 3

if guess != 484 and guess !=-1:
  guess_chances = guess_chances -1
  if guess_chances ==2 and guess !=484 and guess != -1:
    print("Incorect")
    print("Try Again")
    guess=int(input())
    guess_chances=guess_chances -1
  if guess_chances ==1 and guess!= 484 and guess!= -1:
    print("Incorrect")
    print("Final Try")
    guess=int(input())
    guess_chances=guess_chances -1

if guess==484:
  print("Correct")

if guess ==-1:
  print("Goodbye")

if guess_chances== 0:
  print("You have ran out of tries!")
