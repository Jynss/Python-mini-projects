import random

winning_numbers = set()
for numbers in range(6):
    numbers = random.randint(1, 50)
    winning_numbers.add(numbers)

user_guesses=set()

number_of_guesses = 0
print("Enter 6 numbers of your choice, from 1-50 to see if YOU can be the winner of $1000000")
while number_of_guesses < 6:
    guess = int(input())
    number_of_guesses += 1
    user_guesses.add(guess)


correct_guesses =[]

count=0

for guess in user_guesses:
    if guess in winning_numbers:
      count += 1
      correct_guesses.append(guess)

print("You have guessed ", count, " out of the 6 numbers correctly")



if len(correct_guesses) == 6:
    print("Congratulations, you have won yourself $1000000")

