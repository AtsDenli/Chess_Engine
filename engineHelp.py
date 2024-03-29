import numpy as np
import chess

localBoard = chess.Board()

def PNG2Text(game, position, new=False):
    if new == True:
        localBoard.reset()
    moves = []
    for move in game:
        if len(moves) > position:
            break
        moves.append(move)
        localBoard.push_san(move)
    return localBoard

def moveMatrix(board, move, turn):
    piece = ''
    k = 0
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for char in move:
        if move == "O-O" or move == "O-O-O":
            k = 5
        elif char != ' ' and char == char.upper() and char not in numbers:
            piece = char
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
    turn = 0 if turn == 1 else 0
    board.push_san(move)
    stack2 = Text2Stack(board, turn)
    outputBoard = stack2[k]
    return (outputBoard, k)

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

def GetNewBoard(board,stack,k):
    if k == 0:
        board[0][0] = stack
    elif k == 1:
        board[0][1] = stack
    elif k == 2:
        board[0][2] = stack
    elif k == 3:
        board[0][3] = stack
    elif k == 4:
        board[0][4] = stack
    elif k == 5:
        board[0][5] = stack
    return board

def StackToChange(initial, after):
    initStack = []
    outStack = []
    if initial[5] != after[5]:
        initStack = initial[5]
        outStack = after[5]
    if initial[4] != after[4]:
        initStack = initial[4]
        outStack = after[4]
    if initial[3] != after[3]:
        initStack = initial[3]
        outStack = after[3]
    if initial[2] != after[2]:
        initStack = initial[2]
        outStack = after[2]
    if initial[1] != after[1]:
        initStack = initial[1]
        outStack = after[1]

    for i in range(8):
        for j in range(8):
            outStack[i][j] = rounder(initStack[i][j])
            

def rounder(num):
    if num > 0.4:
        return 1
    elif num < -0.4:
        return -1
    else:
        return 0