Player_1 = int(input("Player X it is your turn = "))
Player_2 = int(input("Player O it is your turn ="))

Board=[]

turn_count = 0

while turn_count < 42:
    if turn_count % 2 == 0:
        Player_1 = int(input("Player X it is your turn = "))
        turn_count += 1

    if turn_count % 2 != 0:
        Player_2 = int(input("Player O it is your turn ="))
        turn_count += 1



