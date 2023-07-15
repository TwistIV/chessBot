class GameState():
    def __init__(self):
        self.board = [
            "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
            "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",
            "--", "--", "--", "--", "--", "--", "--", "--",
            "--", "--", "--", "--", "--", "--", "--", "--",
            "--", "--", "--", "--", "--", "--", "--", "--",
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
        return moves

    def getPawnMoves(self, square, moves):
        if self.board[square][0] == 'w' and self.whiteToMove:
            if self.board[square-8] == '--':
                moves.append(Move(square, square-8, self.board))
                if self.board[square-16] == '--' and int(square/8) == 6:
                    moves.append(Move(square, square-16, self.board))
            if self.board[square-9][0] == 'b':
                moves.append(Move(square, square-9, self.board))
            if self.board[square-7][0] == 'b':
                moves.append(Move(square, square-7, self.board))
        elif self.board[square][0] == 'b' and not self.whiteToMove:
            if self.board[square+8] == '--':
                moves.append(Move(square, square+8, self.board))
                if self.board[square+16] == '--' and int(square/8) == 1:
                    moves.append(Move(square, square+16, self.board))
            if self.board[square+9][0] == 'w':
                moves.append(Move(square, square+9, self.board))
            if self.board[square+7][0] == 'w':
                moves.append(Move(square, square+7, self.board))

    def getRookMoves(self):
        pass

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