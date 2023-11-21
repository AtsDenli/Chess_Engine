import torch
import re
import chess

letter2Num = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
num2Letter = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}

def PNG2Text(game):
    moves = []
    re.sub("[i-z]", '', game)
    for move in game.split("  "):
        moves.append(move.split(' '))
    board = chess.Board()
    for move in moves:
        board.push_san(move[0])
        if move[1]:
            board.push_san(move[1])