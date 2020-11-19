import pygame

pygame.init(
width = 950
height = 1200
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect 4')
clock = pygame.time.Clock()
fps = 60
turn_count = 0
#background = pygame.image.load('background.jpg').convert()
running = True
black = 0,0,0
red = 255,0,0
teal  = 0,200,200
green = 0,255,0
turn_count = 0


row1 = [black,black,black,black,black,black,black,black]
row2 = [black,black,black,black,black,black,black,black]
row3 = [black,black,black,black,black,black,black,black]
row4 = [black,black,black,black,black,black,black,black]
row5 = [black,black,black,black,black,black,black,black]
row6 = [black,black,black,black,black,black,black,black]
board = [ row6, row5, row4, row3, row2, row1]







while running:

    pygame.draw.rect(window, pygame.Color('blue'), pygame.Rect(50, 60, 850, 610))

    
    for i in range(8):
         pygame.draw.circle(window, pygame.Color(*row1[i]), (130 + 100*i, 110 ), 40)
         pygame.draw.circle(window, pygame.Color(*row2[i]), (130 + 100*i, 210 ), 40)
         pygame.draw.circle(window, pygame.Color(*row3[i]), (130 + 100*i, 310 ), 40)
         pygame.draw.circle(window, pygame.Color(*row4[i]), (130 + 100*i, 410 ), 40)
         pygame.draw.circle(window, pygame.Color(*row5[i]), (130 + 100*i, 510 ), 40)
         pygame.draw.circle(window, pygame.Color(*row6[i]), (130 + 100*i, 610 ), 40)
                  
       
  


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            #print(mx ,my)

            
           
               #col
             
            if mx > 90 and mx < 175 and turn_count % 2 == 0:
                for i in range(6):
                    if board[i][0] == black:
                      board[i][0] = 255,0,0
                      break
                turn_count +=1

              
            elif mx > 90 and mx < 175 and turn_count % 2 != 0:
                for i in range(6):
                    if board[i][0] == black:
                      board[i][0] = 255,255,0
                      break
                turn_count += 1

                #col2

            if mx > 190 and mx < 275 and turn_count % 2 == 0:
                for i in range(6):
                    if board[i][1] == black:
                      board[i][1] = 255,0,0
                      break
                turn_count +=1

              
            elif mx > 190 and mx < 275 and turn_count % 2 != 0:
                for i in range(6):
                    if board[i][1] == black:
                      board[i][1] = 255,255,0
                      break
                turn_count += 1



                

                
                #col3



            if mx > 290 and mx < 375 and turn_count % 2 == 0:
                for i in range(6):
                    if board[i][2] == black:
                      board[i][2] = 255,0,0
                      break
                turn_count +=1

              
            elif mx > 290 and mx < 375 and turn_count % 2 != 0:
                for i in range(6):
                    if board[i][2] == black:
                      board[i][2] = 255,255,0
                      break
                turn_count += 1
     

                
                #col4

            if mx > 390 and mx < 475 and turn_count % 2 == 0:
                for i in range(6):
                    if board[i][3] == black:
                      board[i][3] = 255,0,0
                      break
                turn_count +=1

              
            elif mx > 390 and mx < 475 and turn_count % 2 != 0:
                for i in range(6):
                    if board[i][3] == black:
                      board[i][3] = 255,255,0
                      break
                turn_count += 1



                
                #col5
            if mx > 490 and mx < 575 and turn_count % 2 == 0:
                for i in range(6):
                    if board[i][4] == black:
                      board[i][4] = 255,0,0
                      break
                turn_count +=1

              
            elif mx > 490 and mx < 575 and turn_count % 2 != 0:
                for i in range(6):
                    if board[i][4] == black:
                      board[i][4] = 255,255,0
                      break
                turn_count += 1
                
                #col6
            if mx > 590 and mx < 675 and turn_count % 2 == 0:
                for i in range(6):
                    if board[i][5] == black:
                      board[i][5] = 255,0,0
                      break
                turn_count +=1

              
            elif mx > 590 and mx < 675 and turn_count % 2 != 0:
                for i in range(6):
                    if board[i][5] == black:
                      board[i][5] = 255,255,0
                      break
                turn_count += 1


            
                #col7
            if mx > 690 and mx < 775 and turn_count % 2 == 0:
                for i in range(6):
                    if board[i][6] == black:
                      board[i][6] = 255,0,0
                      break
                turn_count +=1

              
            elif mx > 690 and mx < 775 and turn_count % 2 != 0:
                for i in range(6):
                    if board[i][6] == black:
                      board[i][6] = 255,255,0
                      break
                turn_count += 1



                
                #col8

            if mx > 790 and mx < 875 and turn_count % 2 == 0:
                for i in range(6):
                    if board[i][7] == black:
                      board[i][7] = 255,0,0
                      break
                turn_count +=1

              
            elif mx > 790 and mx < 875 and turn_count % 2 != 0:
                for i in range(6):
                    if board[i][7] == black:
                      board[i][7] = 255,255,0
                      break
                turn_count += 1    
    clock.tick(fps)
pygame.quit()
quit()




