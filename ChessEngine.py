class GameState():
    def __init__(self):
        self.board = [
            "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
            "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",
            "--", "--", "--", "--", "--", "--", "--", "--",
            "--", "--", "--", "--", "--", "--", "--", "--",
            "--", "--", "--", "wR", "--", "--", "--", "--",
            "--", "--", "--", "--", "--", "--", "--", "--",
            "wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP",
            "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        self.whiteToMove = True
        self.moveLog = []

    #Updates the board when a move is played
    def move(self, move):
        self.board[move.endSq] = move.pieceMoved
        self.board[move.startSq] = "--"
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.endSq] = move.endSquare
            self.board[move.startSq] = move.pieceMoved
            self.whiteToMove = not self.whiteToMove

    #Returns all valid moves
    def getValidMoves(self):
        pass
    
    #Returns all possible piece moves without considering check
    def getAllPieceMoves(self):
        moves = []
        for square in range(len(self.board)):
            piece = self.board[square]
            if piece[1] == 'P':
                self.getPawnMoves(square, moves)
            elif piece[1] == 'R':
                self.getRookMoves(square, moves)
        return moves

    def getPawnMoves(self, square, moves):
        #Generate white pawn moves
        if self.board[square][0] == 'w' and self.whiteToMove:
            if self.board[square-8] == '--':
                moves.append(Move(square, square-8, self.board))
                if self.board[square-16] == '--' and int(square/8) == 6:
                    moves.append(Move(square, square-16, self.board))
            if self.board[square-9][0] == 'b':
                moves.append(Move(square, square-9, self.board))
            if self.board[square-7][0] == 'b':
                moves.append(Move(square, square-7, self.board))

        #Generate black pawn moves
        elif self.board[square][0] == 'b' and not self.whiteToMove:
            if self.board[square+8] == '--':
                moves.append(Move(square, square+8, self.board))
                if self.board[square+16] == '--' and int(square/8) == 1:
                    moves.append(Move(square, square+16, self.board))
            if self.board[square+9][0] == 'w':
                moves.append(Move(square, square+9, self.board))
            if self.board[square+7][0] == 'w':
                moves.append(Move(square, square+7, self.board))

    def getRookMoves(self, square, moves):
        deadEnd = False
        rank = 8 - int(square/8)
        file = square%8 + 1

        if self.board[square][0] == 'w' and self.whiteToMove:#To be removed and add boolean denoting whose piece it is, with logic to take that into account during move gen
            #Left moves
            for space in range(file-1):
                #Square being evaluated
                targetSquare = square-space-1
                if self.board[targetSquare] == '--' or self.board[targetSquare][0] == 'b':
                    moves.append(Move(square, targetSquare, self.board))
                    if self.board[targetSquare][0] == 'b':
                        break
                else:
                    break
            #Right moves
            for space in range(8-file):
                targetSquare = square+space+1
                if self.board[targetSquare] == '--' or self.board[targetSquare][0] == 'b':
                    moves.append(Move(square, targetSquare, self.board))
                    if self.board[targetSquare][0] == 'b':
                        break
                else:
                    break
            #Up moves
            for space in range(8-rank):
                targetSquare = square - (8*(space+1))
                if self.board[targetSquare] == '--' or self.board[targetSquare][0] == 'b':
                    moves.append(Move(square, targetSquare, self.board))
                    if self.board[targetSquare][0] == 'b':
                        break
                else:
                    break
            #Down moves
            for space in range(rank-1):
                targetSquare = square + (8*(space+1))
                print("Square is " + str(square) + " and target square is " + str(targetSquare))
                if self.board[targetSquare] == '--' or self.board[targetSquare][0] == 'b':
                    moves.append(Move(square, targetSquare, self.board))
                    if self.board[targetSquare][0] == 'b':
                        break
                else:
                    break
        

    def getKnightMoves(self):
        pass

    def getBishopMoves(self):
        pass

class Move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startSq = startSq
        self.endSq = endSq
        self.pieceMoved =  board[startSq]
        self.endSquare = board[endSq]

    def __eq__(self, other):
        if isinstance(other, Move):
            pass


    #def getNotation(self):