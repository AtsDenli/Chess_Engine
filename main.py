import pygame
import pieces
import PieceTables

def main():
    BP1 = pieces.Pawn(0, (1,0))
    BP2 = pieces.Pawn(0, (1,1))
    BP3 = pieces.Pawn(0, (1,2))
    BP4 = pieces.Pawn(0, (1,3))
    BP5 = pieces.Pawn(0, (1,4))
    BP6 = pieces.Pawn(0, (1,5))
    BP7 = pieces.Pawn(0, (1,6))
    BP8 = pieces.Pawn(0, (1,7))
    BH1 = pieces.Horse(0, (0,1))
    BH2 = pieces.Horse(0, (0,6))
    BB1 = pieces.Bishop(0, (0,2))
    BB2 = pieces.Bishop(0, (0,5))
    BR1 = pieces.Rook(0, (0,0))
    BR2 = pieces.Rook(0, (0,7))
    BQ = pieces.Queen(0, (0,3))
    BK = pieces.King(0, (0,4))

    WP1 = pieces.Pawn(1, (6,0))
    WP2 = pieces.Pawn(1, (6,1))
    WP3 = pieces.Pawn(1, (6,2))
    WP4 = pieces.Pawn(1, (6,3))
    WP5 = pieces.Pawn(1, (6,4))
    WP6 = pieces.Pawn(1, (6,5))
    WP7 = pieces.Pawn(1, (6,6))
    WP8 = pieces.Pawn(1, (6,7))
    WH1 = pieces.Horse(1, (7,1))
    WH2 = pieces.Horse(1, (7,6))
    WB1 = pieces.Bishop(1, (7,2))
    WB2 = pieces.Bishop(1, (7,5))
    WR1 = pieces.Rook(1, (7,0))
    WR2 = pieces.Rook(1, (7,7))
    WQ = pieces.Queen(1, (7,3))
    WK = pieces.King(1, (7,4))

    board = [[BR1, BH1, BB1, BQ, BK, BB2, BH2, BR1],
             [BP1, BP2, BP3, BP4, BP5, BP6, BP7, BP8], 
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [None, None, None, None, None, None, None, None],
             [WP1, WP2, WP3, WP4, WP5, WP6, WP7, WP8],
             [WR1, WH1, WB1, WQ, WK, WB2, WH2, WR2]]
    
    gameState = 0

    colourRaw = input("Do you want to be black or white?")
    while colourRaw != "black" and colourRaw != "white":
        colourRaw = input("Thats not valid, please write black or white")
    
    if colourRaw == "black":
        colour = 1
    else:
        colour = 0

    gameMoves = []

    while not gameState:
        if colour == 1:
            currentMove = input("Please input your move {source square}-{destination square}")
            gameMoves.append(currentMove.split('-')[1])