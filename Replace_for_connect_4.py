











col1 = [1, 8, 15, 22, 29, 36]
col2 = [2, 9, 16, 23, 30, 37]
col3 = [3, 10, 17, 24, 31, 38]
col4 = [4, 11, 18, 25, 32, 39]
col5 = [5, 12, 19, 26, 33, 40]
col6 = [6, 13, 20, 27, 34, 41]
col7 = [7, 14, 21, 28, 35, 42]
1



turn_count = 0

Player_1 = int(input("Player X it is your turn = "))

Player_2 = 0




#Player_2 = int(input("Player O it is your turn = "))

Board = []



while True:
    if Player_1 == 1:
       turn_count += 1
       for i in range(7):
          if col1[i] != "X" and col1[i] != "O":
              col1[i] = "X"
              print(*col1)
              Player_2 = int(input("Player O it is your turn = "))
              Player_1 = 0
              break







    if Player_2 == 1:
       turn_count += 1
       for i in range(7):
          if col1[i] != "X" and col1[i] != "O":
              col1[i] = "O"
              print(*col1)
              Player_1 = int(input("Player X it is your turn = "))
              Player_2 = 0
              break

    #col2

    if Player_1 == 2:
       turn_count += 1
       for i in range(7):
          if col2[i] != "X" and col2[i] != "O":
              col2[i] = "X"
              print(*col2)
              Player_2 = int(input("Player O it is your turn = "))
              Player_1 = 0
              break




    if Player_2 == 2:
       turn_count += 1
       for i in range(7):
          if col2[i] != "X" and col2[i] != "O":
              col2[i] = "O"
              print(*col2)
              Player_1 = int(input("Player X it is your turn = "))
              Player_2 = 0
              break


#col3
    if Player_1 == 3:
       turn_count += 1
       for i in range(7):
          if col3[i] != "X" and col3[i] != "O":
              col3[i] = "X"
              print(*col3)
              Player_2 = int(input("Player O it is your turn = "))
              Player_1 = 0
              break







    if Player_2 == 3:
       turn_count += 1
       for i in range(7):
          if col3[i] != "X" and col3[i] != "O":
              col3[i] = "O"
              print(*col3)
              Player_1 = int(input("Player X it is your turn = "))
              Player_2 = 0
              break

#col4
    if Player_1 == 4:
       turn_count += 1
       for i in range(7):
          if col4[i] != "X" and col4[i] != "O":
              col4[i] = "X"
              print(*col4)
              Player_2 = int(input("Player O it is your turn = "))
              Player_1 = 0
              break







    if Player_2 == 4:
       turn_count += 1
       for i in range(7):
          if col4[i] != "X" and col4[i] != "O":
              col4[i] = "O"
              print(*col4)
              Player_1 = int(input("Player X it is your turn = "))
              Player_2 = 0
              break

#col5
    if Player_1 == 5:
       turn_count += 1
       for i in range(7):
          if col5[i] != "X" and col5[i] != "O":
              col5[i] = "X"
              print(*col5)
              Player_2 = int(input("Player O it is your turn = "))
              Player_1 = 0
              break







    if Player_2 == 5:
       turn_count += 1
       for i in range(7):
          if col5[i] != "X" and col5[i] != "O":
              col5[i] = "O"
              print(*col5)
              Player_1 = int(input("Player X it is your turn = "))
              Player_2 = 0
              break

#col6
    if Player_1 == 6:
       turn_count += 1
       for i in range(7):
          if col6[i] != "X" and col6[i] != "O":
              col6[i] = "X"
              print(*col6)
              Player_2 = int(input("Player O it is your turn = "))
              Player_1 = 0
              break







    if Player_2 == 6:
       turn_count += 1
       for i in range(7):
          if col6[i] != "X" and col6[i] != "O":
              col6[i] = "O"
              print(*col6)
              Player_1 = int(input("Player X it is your turn = "))
              Player_2 = 0
              break


#col7
    if Player_1 == 7:
       turn_count += 1
       for i in range(7):
          if col7[i] != "X" and col7[i] != "O":
              col7[i] = "X"
              print(*col7)
              Player_2 = int(input("Player O it is your turn = "))
              Player_1 = 0
              break







    if Player_2 == 7:
       turn_count += 1
       for i in range(7):
          if col7[i] != "X" and col7[i] != "O":
              col7[i] = "O"
              print(*col7)
              Player_1 = int(input("Player X it is your turn = "))
              Player_2 = 0
              break



print("Turn Count",turn_count)


