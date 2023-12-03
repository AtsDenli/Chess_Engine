import torch
from torch.utils.data import Dataset, DataLoader
import torch.autograd as AG
from torch import Tensor
import torch.nn as nn
import torch.optim as optim
import re
import numpy as np
import chess
import pandas as pd
import random
import csv

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

    return np.stack((pawn,knight,bishop,rook,queen,king))    

class ChessDataset(Dataset):
    def __init__(self):
        super(ChessDataset,self).__init__()
        self.games = []
        with open("chess_games_edit.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.games.append(row["AN"])


    def __len__(self):
        return 1_248_430
    
    def __getitem__(self):
        noOfGames = 1248430
        index = random.randint(0,noOfGames)
        randGame = self.games[index]
        randGameMoves = randGame.split()