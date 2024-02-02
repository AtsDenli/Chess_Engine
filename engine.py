from torch import save, load
import torch
from torch.utils.data import Dataset, DataLoader
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
        return 200000

    def __getitem__(self,idx):
        noOfGames = 1248430
        idx = random.randint(0,noOfGames)
        randGame = self.games[idx]
        randGame = randGame.split(' ')[1:]
        randGameIndex = random.randint(0,len(randGame)-1)
        randGameMoves = randGame[:randGameIndex]
        if len(randGameMoves) % 2 == 0:
            board = PNG2Text(randGameMoves, randGameIndex)
        else:
            board = PNG2Text(randGameMoves, randGameIndex)
        nextMove = moveMatrix(board, randGame[randGameIndex+1])
        return board, nextMove

data_train = ChessDataset(chessGames)
data_train_loader = DataLoader(data_train, batch_size=32, shuffle=True, drop_last=True)

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
             nn.Conv2d(6, 200, 3, 1, 1),
             nn.Conv2d(200,200,3,1,1),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.SELU(),
             nn.Flatten()
        )


    def forward(self, x):
        return self.model(x)

network = NeuralNetwork().to(device)
optimiser = optim.Adam(network.parameters(),lr=1e-4)

for epoch in range(8):
     for group in data_train_loader:
          X, y = group
          X = X.to(device)
          y = y.to(device)
          prediction = network(X)
          loss = nn.CrossEntropyLoss(prediction, y)

          #backprop
          optimiser.zero_grad()
          loss.backward()
          optimiser.step()
          print(f"Epoch {epoch} complete with loss {loss}")

with open("model_save.pt", "wb") as file:
    save(network.state_dict(),file)