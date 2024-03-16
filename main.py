import chess
import torch
from engine import NeuralNetwork
from engineHelp import Text2Stack, PNG2Text, moveMatrix, GetNewBoard, StackToChange

#THIS FILE IS STILL UNDER PROGRESS

board = chess.Board()
Network = NeuralNetwork
model = torch.load("model_save.pt")
model.eval()

colour = input("Would you like to play black or white?\n")
while colour != "black" and colour != "white":
    colour = input("Would you like to play as black or white?\n")

def pickMove():
    move = ""
    while move not in list(board.legal_moves):
        move = StackToChange(Text2Stack(board), model(board))

def mateInOne(board):
    board = board.copy()
    moves = list(board.legal_moves)
    for move in moves:
        board.push_uci(str(move))
        if board.is_checkmate():
            move = board.pop()
            return move
        board.pop()
    return False

movecount = 0
while not board.is_checkmate():
    if colour == "white":
        whiteMove = input("please input a move in UCI notation\n")
        tmp = mateInOne(board)
        blackMove = tmp if tmp else pickMove()
        board.push_uci(blackMove)
        print(blackMove)
    else:
        tmp = mateInOne(board)
        whiteMove = tmp if tmp else pickMove()
        board.push_uci(whiteMove)
        print(whiteMove)
        blackMove = input("please input a move in UCI notation\n")