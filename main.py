import pygame
import ChessEngine

CELL_SIZE = 100
IMAGES = {}
LIGHT_COLOR = (255, 255, 255)
DARK_COLOR = (102, 153, 153)

'''
Initialize images
'''
def loadImages():
    pieces = ["bP", "bQ", "bK", "bB", "bN", "bR", "wP", "wQ", "wK", "wB", "wN", "wR"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("res/" + piece + ".png"), (CELL_SIZE, CELL_SIZE))


'''
Main method, initialize settings and contains game loop
'''
def main():
    pygame.init()
    window = pygame.display.set_mode((CELL_SIZE*8, CELL_SIZE*8))
    pygame.display.set_caption('5000 ELO Chess AI')
    icon = pygame.image.load("res/icon.png")
    pygame.display.set_icon(icon)

    gameState = ChessEngine.GameState()
    loadImages()

    run = True

    selectedSquare = ()
    moveStartEnd = []
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                col = click[0]//CELL_SIZE
                row = click[1]//CELL_SIZE

                if selectedSquare == (row, col):
                    selectedSquare = ()
                    moveStartEnd = []
                else:
                    selectedSquare = (row, col)
                    moveStartEnd.append(selectedSquare)
                if len(moveStartEnd) == 2:
                    move = ChessEngine.Move(moveStartEnd[0], moveStartEnd[1], gameState.board)
                    gameState.move(move)
                    selectedSquare = ()
                    moveStartEnd = []

                #INPUT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    gameState.undoMove()

        draw(window, gameState)
        pygame.display.update()

    pygame.quit()

def draw(window, gameState):
    drawBoard(window)
    drawPieces(window, gameState.board)

def drawBoard(window):
    window.fill(LIGHT_COLOR)

    isDarkSquare = False
    for x in range(8):
        for y in range(8):
            if isDarkSquare:
                pygame.draw.rect(window, DARK_COLOR, pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            isDarkSquare = not isDarkSquare
        isDarkSquare = not isDarkSquare

def drawPieces(window, board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "--":
                window.blit(IMAGES[piece], pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

main()