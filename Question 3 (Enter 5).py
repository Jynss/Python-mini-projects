print("Enter 5 numbers")
print("Enter number")
number = int(input())
number_list = []
max_number = 5

while max_number <= 5 and max_number != 0:
    number_list.append(number)
    max_number = (max_number - 1)
    if max_number in [4, 3, 2, 1]:
        print("Enter a Number")
        number = int(input())



if 5 not in number_list:
    print("None of these were a 5")

else:
    print("You did enter 5")
