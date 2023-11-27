import torch
import re
import numpy as np
import chess

letter2Num = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
num2Letter = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
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

def Text2Stack(board):
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

    np.stack((pawn,knight,bishop,rook,queen,king))    
