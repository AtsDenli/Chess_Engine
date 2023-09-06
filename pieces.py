class Pawn:
    def __init__(self, colour, position, board):
        self.colour = colour
        self.pos = position
        self.active = True
        self.board = board
    
    def Taken(self):
        self.active = False
        self.pos = None

    def updateBoard(self, newBoard):
        self.board = newBoard

    def FindMoves(self):
        moves = []
        for i in range((-1,2)):
            try:    
                if self.board[self.pos[0], self.pos[1]-i] != None:
                    moves.append((self.pos[0], self.pos[1]-i))
            except IndexError:
                pass
        return moves

class Horse:
    def __init__(self, colour, position, board):
        self.colour = colour
        self.pos = position
        self.active = True

    def Taken(self):
        self.active = False
        self.pos = None

    def updateBoard(self, newBoard):
        self.board = newBoard
    
    def FindMoves(self):
        moves = []
        try:
            if self.board[self.pos[0]-2][self.pos[1]+1] != None:
                moves.append((self.pos[0]-2, self.pos[1]+1))
            if self.board[self.pos[0]-1][self.pos[1]+2] != None:
                moves.append((self.pos[0]-1, self.pos[1]+2))
            if self.board[self.pos[0]+1][self.pos[1]+2] != None:
                moves.append((self.pos[0]+1, self.pos[1]+2))
            if self.board[self.pos[0]+2][self.pos[1]+1] != None:
                moves.append(self.pos[0]+2, self.pos[1]+1)
            if self.board[self.pos[0]+2][self.pos[1]-1] != None:
                moves.append(self.pos[0]+2, self.pos[1]-1)
            if self.board[self.pos[0]+1][self.pos[1]-2] != None:
                moves.append(self.pos[0]+1, self.pos[1]-2)
            if self.board[self.pos[0]-1][self.pos[1]-2] != None:
                moves.append(self.pos[0]-1, self.pos[1]-2)
            if self.board[self.pos[0]-2][self.pos[1]-1] != None:
                moves.append(self.pos[0]-2, self.pos[1]-1)

        except IndexError:
            pass
        return moves

class Bishop:
    def __init__(self, colour, position, board):
        self.colour = colour
        self.pos = position
        self.active = True

    def Taken(self):
        self.active = False
        self.pos = None
    
    def updateBoard(self, newBoard):
        self.board = newBoard

    def FindMoves(self):
        moves = []
        for i in range(1,10):
            try:
                if self.board[self.pos[0]-i][self.pos[1]+i] == None:
                    moves.appen((self.pos[0]-1,self.pos[1]+i))
                else:
                    break
            except IndexError:
                break

        for i in range(1,10):
            try:
                if self.board[self.pos[0]-i][self.pos[1]-i] == None:
                    moves.appen((self.pos[0]-1,self.pos[1]+i))
                else:
                    break
            except IndexError:
                break
        
        for i in range(1,10):
            try:
                if self.board[self.pos[0]+i][self.pos[1]+i] == None:
                    moves.appen((self.pos[0]-1,self.pos[1]+i))
                else:
                    break
            except IndexError:
                break
        
        for i in range(1,10):
            try:
                if self.board[self.pos[0]+i][self.pos[1]-i] == None:
                    moves.appen((self.pos[0]-1,self.pos[1]+i))
                else:
                    break
            except IndexError:
                break

        return moves


class Rook:
    def __init__(self, colour, position, board):
        self.colour = colour
        self.pos = position
        self.active = True

    def Taken(self):
        self.active = False
        self.pos = None

    def updateBoard(self, newBoard):
        self.board = newBoard
    
    def FindMoves(self):
        moves = []
        for i in range(7):
            try:
                if self.board[self.pos[0]][i+self.pos[1]]:
                    moves.append((self.pos[0],self.pos[1]+i))
            except IndexError:
                break
        
        for i in range(7):
            try:
                if self.board[self.pos[0]][self.pos[1]-i]:
                    moves.append((self.pos[0],self.pos[1]+i))
            except IndexError:
                break

        for i in range(7):
            try:
                if self.board[self.pos[0]+i][self.pos[1]]:
                    moves.append((self.pos[0]+1, self.pos[1]))
            except IndexError:
                break

        for i in range(7):
            try:
                if self.board[self.pos[0]]-1[self.pos[1]]:
                    moves.append((self.pos[0],self.pos[1]))
            except IndexError:
                break
        
        return moves

class Queen:
    def __init__(self, colour, position, board):
        self.colour = colour
        self.pos = position
        self.active = True

    def Taken(self):
        self.active = False
        self.pos = None

    def updateBoard(self, newBoard):
        self.board = newBoard
    
    def FindMoves(self):
        moves = []
        for i in range(7):
            try:
                if self.board[self.pos[0]][i+self.pos[1]]:
                    moves.append((self.pos[0],self.pos[1]+i))
            except IndexError:
                break
        
        for i in range(7):
            try:
                if self.board[self.pos[0]][self.pos[1]-i]:
                    moves.append((self.pos[0],self.pos[1]+i))
            except IndexError:
                break

        for i in range(7):
            try:
                if self.board[self.pos[0]+i][self.pos[1]]:
                    moves.append((self.pos[0]+1, self.pos[1]))
            except IndexError:
                break

        for i in range(7):
            try:
                if self.board[self.pos[0]]-1[self.pos[1]]:
                    moves.append((self.pos[0],self.pos[1]))
            except IndexError:
                break
        
        for i in range(1,10):
            try:
                if self.board[self.pos[0]-i][self.pos[1]+i] == None:
                    moves.appen((self.pos[0]-1,self.pos[1]+i))
                else:
                    break
            except IndexError:
                break

        for i in range(1,10):
            try:
                if self.board[self.pos[0]-i][self.pos[1]-i] == None:
                    moves.appen((self.pos[0]-1,self.pos[1]+i))
                else:
                    break
            except IndexError:
                break
        
        for i in range(1,10):
            try:
                if self.board[self.pos[0]+i][self.pos[1]+i] == None:
                    moves.appen((self.pos[0]-1,self.pos[1]+i))
                else:
                    break
            except IndexError:
                break
        
        for i in range(1,10):
            try:
                if self.board[self.pos[0]+i][self.pos[1]-i] == None:
                    moves.appen((self.pos[0]-1,self.pos[1]+i))
                else:
                    break
            except IndexError:
                break

        return moves
        

class King:
    def __init__(self, colour, position, board):
        self.colour = colour
        self.pos = position
        self.active = True

    def Taken(self):
        self.active = False
        self.pos = None

    def updateBoard(self, newBoard):
        self.board = newBoard
    
    def FindMoves(self):
        moves = []
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    if(self.board[self.pos[0]-i][self.pos[1]-j]) == None and i != 0 and j != 0:
                        moves.append(self.board[self.pos[0]-i][self.pos[1]-j])
                except IndexError:
                    pass
        return moves