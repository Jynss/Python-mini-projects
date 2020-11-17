def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

user_list = []

print("Create a list and I'll tell you how many prime numbers are in it. Type -1 when you are  done  ")
number = int(input())
while number !=-1:
    number = int(input())
    user_list.append(number)

print("\n"*4)

def is_prime_ception(list):
    count = 0
    for x in range(len(list)):
        if is_prime(list[x]):
            count += 1

    print(count)


is_prime_ception(user_list)
