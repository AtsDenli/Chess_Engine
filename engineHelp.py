import re
import numpy as np
import chess

board = chess.Board()

def PNG2Text(game, position):
    moves = []
    re.sub("[i-z]", '', game)
    for move in game.split("  "):
        if len(moves) > position:
            break
        moves.append(move.split(' '))
    for move in moves:
        board.push_san(move[0])
        if move[1]:
            board.push_san(move[1])
    return board

def moveMatrix(board, move):
    piece = ''
    for char in move:
        if char != ' ' and char == char.upper():
            piece = char
    stack = Text2Stack(board)
    k = 0
    if piece == '':
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
    board.push_san(move)
    stack2 = Text2Stack(board)
    outputBoard = stack2[k]
    return (initialBoard, outputBoard)

def Text2Stack(board,flip=1):
    arraySize = (8,8)
    pawn = np.zeros(arraySize, dtype=int)
    knight = np.zeros(arraySize, dtype=int)
    bishop = np.zeros(arraySize, dtype=int)
    rook = np.zeros(arraySize, dtype=int)
    queen = np.zeros(arraySize, dtype=int)
    king = np.zeros(arraySize, dtype=int)
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

    return np.stack((pawn,knight,bishop,rook,queen,king)) if flip == 1 else np.stack((flip(pawn), flip(knight), flip(bishop), flip(rook), flip(queen), flip(king)))

