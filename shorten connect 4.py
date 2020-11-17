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
  if turn_count == 0:
  pass
