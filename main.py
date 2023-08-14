import pygame
import ChessEngine

CELL_SIZE = 100
IMAGES = {}
LIGHT_COLOR = (255, 255, 255)
DARK_COLOR = (102, 153, 153)
HIGHLIGHT_COLOR = (204, 204, 255)

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

    loadImages()

    gameState = ChessEngine.GameState()
    validMoves = gameState.getAllPieceMoves()

    run = True
    awaitingMove = True

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
                    moveStartEnd.append((row*8)+col)
                if len(moveStartEnd) == 2:
                    move = ChessEngine.Move(moveStartEnd[0], moveStartEnd[1], gameState.board)
                    for validMove in validMoves:
                        if validMove.startSq == move.startSq and validMove.endSq == move.endSq:
                            gameState.move(move)
                            awaitingMove = False

                    selectedSquare = ()
                    moveStartEnd = []

                #INPUT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    gameState.undoMove()
                    validMoves = gameState.getAllPieceMoves()

        if not awaitingMove:
            validMoves = gameState.getAllPieceMoves()
            awaitingMove = True

        draw(window, validMoves, moveStartEnd, gameState)
        pygame.display.update()

    pygame.quit()

def draw(window, validMoves, moveStartEnd, gameState):
    drawBoard(window)
    drawMoves(window, validMoves, moveStartEnd)
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

def drawMoves(window, validMoves, moveStartEnd):
    if len(moveStartEnd) == 1:
        for move in validMoves:
            if move.startSq == moveStartEnd[0]:
                rank = 8 - int(move.endSq/8)
                file = move.endSq%8
                print("Rank is " + str(rank) + "  and file is " + str(file))
                print(move.startSq)
                print(len(validMoves))
                pygame.draw.rect(window, HIGHLIGHT_COLOR, pygame.Rect(file*CELL_SIZE, (8-rank)*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def drawPieces(window, board):
    for row in range(8):
        for col in range(8):
            piece = board[(row*8)+col]
            if piece != "--":
                window.blit(IMAGES[piece], pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

main()