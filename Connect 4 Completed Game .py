board=["|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"]
board2=["|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"]
board3=["|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"]
board4=["|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"]
board5=["|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"]
board6=["|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"]


turn_count = 0

entire_board = [board,board2,board3,board4,board5,board6,]
for row in entire_board:
    print(*row)

Player_1 = int(input("Player X it is your turn "))
Player_2 = 0




while True:

    if Player_1 == 1:
        turn_count += 1
        for row in entire_board:
            if row[1] != "X" and row[1] != "O":
                row[1] = "X"
                for row in reversed((entire_board)):
                    print(*row)
                Player_2 = int(input("Player O it is your turn = "))
                Player_1 = 0
                break

    if Player_2 == 1:
        turn_count += 1
        for row in entire_board:
            if row[1] != "X" and row[1] != "O":
                row[1] = "O"
                for row in reversed(entire_board):
                    print(*row)
                Player_1 = int(input("Player X it is your turn = "))
                Player_2 = 0
                break

    if Player_1 == 2:
        turn_count += 1
        for row in entire_board:
            if row[3] != "X" and row[3] != "O":
                row[3] = "X"
                for row in reversed(entire_board):
                    print(*row)
                Player_2 = int(input("Player O it is your turn = "))
                Player_1 = 0
                break

    if Player_2 == 2:
        turn_count += 1
        for row in entire_board:
            if row[3] != "X" and row[3] != "O":
                row[3] = "O"
                for row in reversed(entire_board):
                    print(*row)
                Player_1 = int(input("Player X it is your turn = "))
                Player_2 = 0
                break

#col3
    if Player_1 == 3:
        turn_count += 1
        for row in entire_board:
            if row[5] != "X" and row[5] != "O":
                row[5] = "X"
                for row in reversed(entire_board):
                    print(*row)
                Player_2 = int(input("Player O it is your turn = "))
                Player_1 = 0
                break

    if Player_2 == 3:
        turn_count += 1
        for row in entire_board:
            if row[5] != "X" and row[5] != "O":
                row[5] = "O"
                for row in reversed(entire_board):
                    print(*row)
                Player_1 = int(input("Player X it is your turn = "))
                Player_2 = 0
                break

#col4
    if Player_1 == 4:
        turn_count += 1
        for row in entire_board:
            if row[7] != "X" and row[7] != "O":
                row[7] = "X"
                for row in reversed(entire_board):
                    print(*row)
                Player_2 = int(input("Player O it is your turn = "))
                Player_1 = 0
                break

    if Player_2 == 4:
        turn_count += 1
        for row in entire_board:
            if row[7] != "X" and row[7] != "O":
                row[7] = "O"
                for row in reversed(entire_board):
                    print(*row)
                Player_1 = int(input("Player X it is your turn = "))
                Player_2 = 0
                break

#col5
    if Player_1 == 5:
        turn_count += 1
        for row in entire_board:
            if row[9] != "X" and row[9] != "O":
                row[9] = "X"
                for row in reversed(entire_board):
                    print(*row)
                Player_2 = int(input("Player O it is your turn = "))
                Player_1 = 0
                break

    if Player_2 == 5:
        turn_count += 1
        for row in entire_board:
            if row[9] != "X" and row[9] != "O":
                row[9] = "O"
                for row in reversed(entire_board):
                    print(*row)
                Player_1 = int(input("Player X it is your turn = "))
                Player_2 = 0
                break

#col6
    if Player_1 == 6:
        turn_count += 1
        for row in entire_board:
            if row[11] != "X" and row[11] != "O":
                row[11] = "X"
                for row in reversed(entire_board):
                    print(*row)
                Player_2 = int(input("Player O it is your turn = "))
                Player_1 = 0
                break

    if Player_2 == 6:
        turn_count += 1
        for row in entire_board:
            if row[11] != "X" and row[11] != "O":
                row[11] = "O"
                for row in reversed(entire_board):
                    print(*row)
                Player_1 = int(input("Player X it is your turn = "))
                Player_2 = 0
                break

#col7
    if Player_1 == 7:
        turn_count += 1
        for row in entire_board:
            if row[13] != "X" and row[13] != "O":
                row[13] = "X"
                for row in reversed(entire_board):
                    print(*row)
                Player_2 = int(input("Player O it is your turn = "))
                Player_1 = 0
                break

    if Player_2 == 7:
        turn_count += 1
        for row in entire_board:
            if row[13] != "X" and row[13] != "O":
                row[13] = "O"
                for row in reversed(entire_board):
                    print(*row)
                Player_1 = int(input("Player X it is your turn = "))
                Player_2 = 0
                break
