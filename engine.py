import torch
from torch.utils.data import Dataset, DataLoader
import torch.autograd as AG
from torch import Tensor
import torch.nn as nn
import torch.optim as optim
import random
import csv
from engineHelp import Text2Stack, PNG2Text, moveMatrix

chessGames = []
with open("chess_games_edit.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                chessGames.append(row["AN"])

device = "cuda" if torch.cuda.is_available() else "cpu"

class ChessDataset(Dataset):
    def __init__(self,games):
        super(ChessDataset,self).__init__()
        self.games = games
        
    def __len__(self):
        return 1_248_430
    
    def __getitem__(self):
        noOfGames = 1248430
        index = random.randint(0,noOfGames)
        randGame = self.games[index]
        randGameIndex = random.randint(0,len(randGame)-1)
        randGameMoves = randGame[:randGameIndex]
        if len(randGameMoves) % 2 == 0:
            board = Text2Stack(PNG2Text(randGameMoves),-1)
        else:
            board = Text2Stack(PNG2Text(randGameMoves))
        nextMove = moveMatrix(board, randGame[randGameIndex+1])
        return board, nextMove
    
data_train = ChessDataset(chessGames)
data_train_loader = DataLoader(data_train, batch_size=32, shuffle=True, drop_last=True)

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

    def forward():
        pass