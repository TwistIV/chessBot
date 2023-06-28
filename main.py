import pygame

pygame.init()

CELL_SIZE = 100

window = pygame.display.set_mode((CELL_SIZE*8, CELL_SIZE*8))
pygame.display.set_caption('5000 ELO Chess AI')

icon = pygame.image.load("res/icon.png")
pygame.display.set_icon(icon)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        window.fill((255, 255, 255))

        isDarkSquare = False
        for x in range(8):
            for y in range(8):
                if isDarkSquare:
                    pygame.draw.rect(window,(0,0,0), (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
                isDarkSquare = not isDarkSquare
            isDarkSquare = not isDarkSquare
        pygame.display.update()

pygame.quit()