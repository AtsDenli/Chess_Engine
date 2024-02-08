import re
import numpy as np
import chess

board = chess.Board()

def PNG2Text(game, position, new=False):
    if new == True:
        board.reset()
    moves = []
    for move in game:
        if len(moves) > position:
            break
        moves.append(move)
        board.push_san(move)
    return board

def moveMatrix(board, move, turn):
    piece = ''
    k = 0
    for char in move:
        if move == "O-O" or move == "O-O-O":
            k = 5
        elif char != ' ' and char == char.upper():
            piece = char
    stack = Text2Stack(board, turn)
    if k == 5:
        pass
    elif piece == '':
        k = 0
    elif piece == 'N':
        k = 1
    elif piece == 'B':
        k = 2
    elif piece == 'R':
        k = 3
    elif piece == 'Q':
        k = 4
    elif piece == 'K':
        k = 5

    initialBoard = stack[k]
    turn = 0 if turn == 1 else 0
    board.push_san(move)
    stack2 = Text2Stack(board, turn)
    outputBoard = stack2[k]
    return (initialBoard, outputBoard)

def Text2Stack(board,turn=1):
    arraySize = (8,8)
    board = make_2D(board)
    pawn = np.zeros(arraySize, dtype=np.float32)
    knight = np.zeros(arraySize, dtype=np.float32)
    bishop = np.zeros(arraySize, dtype=np.float32)
    rook = np.zeros(arraySize, dtype=np.float32)
    queen = np.zeros(arraySize, dtype=np.float32)
    king = np.zeros(arraySize, dtype=np.float32)
    for i in range(7):
        for j in range(7):
            if board[i][j].lower() == 'p':
                pawn[i][j] = 1 if board[i][j] == 'P' else -1
            elif board[i][j].lower() == 'n':
                knight[i][j] = 1 if board[i][j] == 'N' else -1
            elif board[i][j].lower() == 'b':
                bishop[i][j] = 1 if board[i][j] == 'B' else -1
            elif board[i][j].lower() == 'r':
                rook[i][j] = 1 if board[i][j] == 'R' else -1
            elif board[i][j].lower() == 'q':
                queen[i][j] = 1 if board[i][j] == 'Q' else -1
            elif board[i][j].lower() == 'k':
                king[i][j] = 1 if board[i][j] == 'K' else -1

    return np.stack((pawn,knight,bishop,rook,queen,king)) if turn == 1 else np.stack((np.flip(pawn), np.flip(knight), np.flip(bishop), np.flip(rook), np.flip(queen), np.flip(king)))

#This function is from StackOverflow
def make_2D(board): 
    pgn = board.epd()
    newBoard = []  #Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        tmp = []  #This is the row I make
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    tmp.append('.')
            else:
                tmp.append(thing)
        newBoard.append(tmp)
    return newBoard