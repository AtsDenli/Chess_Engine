import pieces
import PieceTables
import search_util as SU
import notation as no

def main():

    #making the peices accessible to all functions
    global BP1, BP2, BP3, BP4, BP5, BP6, BP7, BP8, BH1, BH2, BB1, BB2, BR1, BR2, BQ, BK
    global WP1, WP2, WP3, WP4, WP5, WP6, WP7, WP8, WH1, WH2, WB1, WB2, WR1, WR2, WQ, WK

    board = [[BR1, BH1, BB1, BQ, BK, BB2, BH2, BR1],
            [BP1, BP2, BP3, BP4, BP5, BP6, BP7, BP8], 
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [WP1, WP2, WP3, WP4, WP5, WP6, WP7, WP8],
            [WR1, WH1, WB1, WQ, WK, WB2, WH2, WR2]]

    BP1 = pieces.Pawn(0, (1,0),board)
    BP2 = pieces.Pawn(0, (1,1),board)
    BP3 = pieces.Pawn(0, (1,2),board)
    BP4 = pieces.Pawn(0, (1,3),board)
    BP5 = pieces.Pawn(0, (1,4),board)
    BP6 = pieces.Pawn(0, (1,5),board)
    BP7 = pieces.Pawn(0, (1,6),board)
    BP8 = pieces.Pawn(0, (1,7),board)
    BH1 = pieces.Horse(0, (0,1),board)
    BH2 = pieces.Horse(0, (0,6),board)
    BB1 = pieces.Bishop(0, (0,2),board)
    BB2 = pieces.Bishop(0, (0,5),board)
    BR1 = pieces.Rook(0, (0,0),board)
    BR2 = pieces.Rook(0, (0,7),board)
    BQ = pieces.Queen(0, (0,3),board)
    BK = pieces.King(0, (0,4),board)

    WP1 = pieces.Pawn(1, (6,0),board)
    WP2 = pieces.Pawn(1, (6,1),board)
    WP3 = pieces.Pawn(1, (6,2),board)
    WP4 = pieces.Pawn(1, (6,3),board)
    WP5 = pieces.Pawn(1, (6,4),board)
    WP6 = pieces.Pawn(1, (6,5),board)
    WP7 = pieces.Pawn(1, (6,6),board)
    WP8 = pieces.Pawn(1, (6,7),board)
    WH1 = pieces.Horse(1, (7,1),board)
    WH2 = pieces.Horse(1, (7,6),board)
    WB1 = pieces.Bishop(1, (7,2),board)
    WB2 = pieces.Bishop(1, (7,5),board)
    WR1 = pieces.Rook(1, (7,0),board)
    WR2 = pieces.Rook(1, (7,7),board)
    WQ = pieces.Queen(1, (7,3),board)
    WK = pieces.King(1, (7,4),board)
    
    # A record of all the moves played
    record = []
    gameState = 0

    while not gameState:
        currentMove = input("Enter your move {current position}-{new position}")
        startingPos, endingPos = currentMove.split('-')[0], currentMove.split('-')[1]
        startCoords = no.fromNotation(startingPos)
        endCoords = no.fromNotation(endingPos)
        if endCoords in board[startCoords[0], startCoords[1]].FindMoves():
            board[endCoords[0], endCoords[1]] = board[startCoords[0], startCoords[1]]
            board[startCoords[0],startCoords[1]] = None
            record.append(currentMove)
        # Now the computer plays its moves
