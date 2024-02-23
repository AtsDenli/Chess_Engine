import chess
import engine
import torch
from engineHelp import Text2Stack, PNG2Text, moveMatrix, GetNewBoard

#THIS FILE IS STILL UNDER PROGRESS

board = chess.Board()
model = engine.NeuralNetwork()
model.load_state_dict(torch.load("model_save.pt"))

colour = input("Would you like to play black or white?")
while colour != "black" or colour != "white":
    colour = input("Would you like to play as black or white?")

def pickMove():
    Text2Stack(PNG2Text(board))

movecount = 0
while not board.is_checkmate():
    if colour == "white":
        whiteMove = input("please input a move in standard algebraic notation")
        while True:
            try:
                board.push_san(whiteMove)
                break
            except Exception:
                print("Please input valid standard algebraic notation")
    blackMove = pickMove()   