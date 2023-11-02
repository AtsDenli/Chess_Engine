import PieceTables as PT
import search_util as SU
import notation as NO

def eval(board):
    WEval = 0
    BEval = 0
    for row in board:
        for piece in row:
            if piece.active:
                WEval += piece.points if piece.colour == 1 else 0
                BEval += piece.points if piece.colour == 0 else 0


def search():
    pass