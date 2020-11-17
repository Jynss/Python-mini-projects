import pygame

pygame.init()
width = 900
height = 1200
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect 4')
clock = pygame.time.Clock()
fps = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            # Enter code to place a peg into the board
            # The mouse_pos_x variable is the horizontal location of the mouse in pixels when the person clicked
            # This code must use the mouse_pos_x variable to determine which column to place the peg
    # Enter code to display the board
    # This is how you display a rectangle
    # The four numbers in the Rect function are the x location, y location, width and height of the rectangle in pixels
    pygame.draw.rect(window, pygame.Color('blue'), pygame.Rect(50, 60, 800, 600))
    # This is how you draw a circle
    # The three numbers represent the x location, y location, and the radius of the circle
    pygame.draw.circle(window, pygame.Color('grey'), (190, 200), 40)

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
