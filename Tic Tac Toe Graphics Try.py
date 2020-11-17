
import pygame

pygame.init()
width = 800
height = 900
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
fps = 60
black = (0,0,0)
teal  = 0,200,200
turn_count = 0
running = True

image1 = pygame.image.load(r'C:\Users\User\OneDrive\Desktop\Orbtronics\Big X.jpg')
image2 = pygame.image.load(r'C:\Users\User\OneDrive\Desktop\Orbtronics\Big O.jpg')

def board():
   pygame.draw.rect(window, pygame.Color('blue'), pygame.Rect(250, 0, 20, 900))
   pygame.draw.rect(window, pygame.Color('blue'), pygame.Rect(540, 0, 20, 900))
   pygame.draw.rect(window, pygame.Color('blue'), pygame.Rect(0, 240, 800, 20))
   pygame.draw.rect(window, pygame.Color('blue'), pygame.Rect(0, 500, 800, 20))

  
while running:
    board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx,my)
                                #row 1
            if mx > 0 and mx < 240 and my < 240 and my > 0 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(60,60))

            elif mx > 0 and mx < 240 and my < 240 and my > 0 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(60,60))

            if mx > 260 and mx < 550 and my < 240 and my > 0 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(350,60))

            elif mx > 260 and mx < 550 and my < 240 and my > 0 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(350,60))

            
            if mx > 600 and mx < 800 and my < 240 and my > 0 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(620,60))

            elif mx > 600 and mx < 800 and my < 240 and my > 0 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(620,60))
                              #row2
            if mx > 0 and mx < 250 and my < 500 and my > 260 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(70,328))

            elif mx > 0 and mx < 250 and my < 500 and my > 260 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(70,328))

            if mx > 270 and mx < 540 and my < 500 and my > 260 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(355,328))

            elif mx > 270 and mx < 540 and my < 500 and my > 260 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(355,328))

            if mx > 600 and mx < 800 and my < 500 and my > 260 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(620,328))

            elif mx > 600 and mx < 800 and my < 500 and my > 260 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(620,328))
                          #row3
                
            if mx > 0 and mx < 240 and my < 900 and my > 520 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(75,590))

            elif mx > 0 and mx < 240 and my < 900 and my > 520 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(75,590))

            if mx > 270 and mx < 540 and my < 900 and my > 520 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(350,590))

            elif mx > 270 and mx < 540 and my < 900 and my > 520 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(350,590))

            if mx > 600 and mx < 800 and my < 900 and my > 520 and turn_count % 2 == 0:
                turn_count +=1
                window.blit(image1,(620,590))

            elif mx > 600 and mx < 800 and my < 900 and my > 520 and turn_count % 2 != 0:
                turn_count +=1
                window.blit(image2,(620,590))         
            
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
















