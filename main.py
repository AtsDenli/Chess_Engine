import chess
import torch
from engine import NeuralNetwork
from engineHelp import Text2Stack, PNG2Text, moveMatrix, GetNewBoard, StackToChange

#THIS FILE IS STILL UNDER PROGRESS

board = chess.Board()
Network = NeuralNetwork
model = torch.load("model_save.pt")
model.eval()

colour = input("Would you like to play black or white?")
while colour != "black" or colour != "white":
    colour = input("Would you like to play as black or white?")

def pickMove():
    move = ""
    while move not in list(board.legal_moves):
        move = StackToChange(Text2Stack(board), model(board))

def mateInOne(board):
    board = board.copy()
    moves = list(board.legal_moves)
    for move in moves:
        board.push_uci(move)
        if board.is_checkmate():
            move = board.pop()
            return move
        board.pop()
    return False

movecount = 0
while not board.is_checkmate():
    if colour == "white":
        whiteMove = input("please input a move in UCI notation")
        while True:
            try:
                board.push_uci(whiteMove)
                break
            except Exception:
                print("Please input valid UCI notation")
        tmp = mateInOne(board)
        blackMove = tmp if tmp else pickMove()
        board.push_uci(blackMove)
        print(blackMove)
    else:
        tmp = mateInOne(board)
        whiteMove = tmp if tmp else pickMove()
        board.push_uci(whiteMove)
        print(whiteMove)
        blackMove = input("please input a move in UCI notation")
        while True:
            try:
                board.push_uci(blackMove)
                break
            except Exception:
                print("please input valid UCI notation")