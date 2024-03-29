from torch import save, load
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import random
import csv
from engineHelp import Text2Stack, PNG2Text, moveMatrix, GetNewBoard

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
        idx = random.randint(0,noOfGames-4)
        randGame = self.games[idx]
        randGame = randGame.split(' ')[1:]
        randGameIndex = random.randint(0,len(randGame)-4)
        randGameMoves = randGame[:randGameIndex]
        # 1 if white's turn
        turn = 1 if randGameIndex % 2 == 1 else 0
        board = PNG2Text(randGameMoves, randGameIndex-1, True)
        nextMove = moveMatrix(board, randGame[randGameIndex], turn)
        board = Text2Stack(board, turn)
        return board, nextMove

data_train = ChessDataset(chessGames)
data_train_loader = DataLoader(data_train, batch_size=1, shuffle=True, drop_last=True)

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
             nn.Conv2d(6, 200, 3, 1, 1),
             nn.BatchNorm2d(200),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.BatchNorm2d(200),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.BatchNorm2d(200),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.BatchNorm2d(200),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.BatchNorm2d(200),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.BatchNorm2d(200),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.BatchNorm2d(200),
             nn.SELU(),
             nn.Conv2d(200,200,3,1,1),
             nn.BatchNorm2d(200),
             nn.SELU(),
             nn.Conv2d(200,6,3,1,1),
             nn.SELU(),
             #nn.Flatten()
        )

    def forward(self, x):
        return self.model(x)

if __name__ == "__main__":
    network = NeuralNetwork().to(device)
    optimiser = optim.Adam(network.parameters(),lr=1e-4)

    for epoch in range(125):
        for group in data_train_loader:
            X = group[0].to(device)
            value = GetNewBoard(X, group[1][0], group[1][1])[0]
            prediction = network(X)[0]
            metric_from = nn.CrossEntropyLoss()
            metric_to = nn.CrossEntropyLoss()
            loss_from = metric_from(value[:,0,:], prediction[:,0,:])
            loss_to = metric_to(value[:,1,:], prediction[:,1,:])
            loss = loss_from + loss_to
            #backprop
            optimiser.zero_grad()
            loss.backward()
            optimiser.step()
        print(f"Epoch {epoch} complete with loss {loss}")

    with open("model_save.pt", "wb") as file:
        save(network,file)