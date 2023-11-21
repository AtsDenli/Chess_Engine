import chess
import engine

board = chess.Board()

colour = input("Would you like to play black or white?")
while colour != "black" or colour != "white":
    colour = input("Would you like to play as black or white?")

while not board.is_checkmate():
    pass