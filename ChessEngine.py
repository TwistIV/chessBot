class GameState():
    def __init__(self):
        self.board = [
            "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
            "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",
            "--", "--", "--", "--", "--", "bN", "--", "--",
            "--", "--", "--", "--", "--", "--", "--", "--",
            "--", "--", "--", "wR", "wB", "--", "--", "--",
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
                self.getCardinalMoves(square, moves)
            elif piece[1] == 'B':
                self.getDiagnoalMoves(square, moves)
            elif piece[1] == 'Q':
                self.getCardinalMoves(square, moves)
                self.getDiagnoalMoves(square, moves)
            elif piece[1] == 'N':
                self.getKnightMoves(square, moves)
            elif piece[1] == 'K':
                self.getKingMoves(square, moves)
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

    def getCardinalMoves(self, square, moves):
        rank = 8 - int(square/8)
        file = square%8 + 1

        if self.whiteToMove:
            otherPlayer = 'b'
        else:
            otherPlayer = 'w'

        if self.board[square][0] == otherPlayer:
            return

        #Left moves
        for space in range(file-1):
            #Square being evaluated
            targetSquare = square-space-1
            if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                moves.append(Move(square, targetSquare, self.board))
                if self.board[targetSquare][0] == otherPlayer:
                    break
            else:
                break
        #Right moves
        for space in range(8-file):
            targetSquare = square+space+1
            if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                moves.append(Move(square, targetSquare, self.board))
                if self.board[targetSquare][0] == otherPlayer:
                    break
            else:
                break
        #Up moves
        for space in range(8-rank):
            targetSquare = square - (8*(space+1))
            if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                moves.append(Move(square, targetSquare, self.board))
                if self.board[targetSquare][0] == otherPlayer:
                    break
            else:
                break
        #Down moves
        for space in range(rank-1):
            targetSquare = square + (8*(space+1))
            if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                moves.append(Move(square, targetSquare, self.board))
                if self.board[targetSquare][0] == otherPlayer:
                    break
            else:
                break
        
    def getDiagnoalMoves(self, square, moves):
        rank = 8 - int(square/8)
        file = square%8 + 1

        if self.whiteToMove:
            otherPlayer = 'b'
        else:
            otherPlayer = 'w'

        if self.board[square][0] == otherPlayer:
            return

        #Up left moves
        for space in range(min([file-1, 8-rank])):
            #Square being evaluated
            targetSquare = square - (9*(space+1))
            if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                moves.append(Move(square, targetSquare, self.board))
                if self.board[targetSquare][0] == otherPlayer:
                    break
            else:
                break
        #Up right moves
        for space in range(min([8-file, 8-rank])):
            targetSquare = square - (7*(space+1))
            if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                moves.append(Move(square, targetSquare, self.board))
                if self.board[targetSquare][0] == otherPlayer:
                    break
            else:
                break
        #Down left moves
        for space in range(min([file-1, rank-1])):
            targetSquare = square + (7*(space+1))
            if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                moves.append(Move(square, targetSquare, self.board))
                if self.board[targetSquare][0] == otherPlayer:
                    break
            else:
                break
        #Down right moves
        for space in range(min([8-file, rank-1])):
            targetSquare = square + (9*(space+1))
            if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                moves.append(Move(square, targetSquare, self.board))
                if self.board[targetSquare][0] == otherPlayer:
                    break
            else:
                break

    def getKnightMoves(self, square, moves):
        offsets = [6, 10, 15, 17]

        if self.whiteToMove:
            otherPlayer = 'b'
        else:
            otherPlayer = 'w'

        if self.board[square][0] == otherPlayer:
            return
        
        #Loop runs twice to get knight moves both above the piece and below
        for x in range(2):
            for offset in offsets:
                targetSquare = square - offset
                if targetSquare < 0 or targetSquare > 63:
                    continue
                else:
                    if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                        moves.append(Move(square, targetSquare, self.board))
            #Multiplies offsets by -1 to get the other half of knight moves
            for index, offset in enumerate(offsets):
                offsets[index] = offset * -1

    def getKingMoves(self, square, moves):
        offsets = [1, 7, 8, 9]

        if self.whiteToMove:
            otherPlayer = 'b'
        else:
            otherPlayer = 'w'

        if self.board[square][0] == otherPlayer:
            return
        
        #Loop runs twice to get king moves both above the piece and below
        for x in range(2):
            for offset in offsets:
                targetSquare = square - offset
                if targetSquare < 0 or targetSquare > 63:
                    continue
                else:
                    if self.board[targetSquare] == '--' or self.board[targetSquare][0] == otherPlayer:
                        moves.append(Move(square, targetSquare, self.board))
            #Multiplies offsets by -1 to get the other half of king moves
            for index, offset in enumerate(offsets):
                offsets[index] = offset * -1

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