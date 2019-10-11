import numpy as np


class BoardGame:
    def __init__(self, squares, row, column):
        self.board = np.zeros((squares,row,column))
        self.start_game()
    def drop_piece(self, row, col, board):
        self.quad = -99
        if self.row > 3 and self.col > 3:
            self.quad = 3
            self.row = row - 4
            self.col = col - 4
        elif col > 3:
            self.quad = 1
            self.col = col - 4
            self.row = row - 1
        elif row > 3:
            self.quad = 2
            self.col = col - 1
            self.row = row - 4
        else:
            self.quad = 0
            self.row = row - 1
            self.col = col - 1
        
        print(self.turn) 
        
        if self.turn ==0:
            self.piece = 1
        else:
            self.piece = 2
        
        if not self.valid_move(self.row, self.col, self.quad):
            print("Space is already occupied, select another place")
            return 
        else:
            self.turn += 1
            print(self.turn)
            self.turn = self.turn % 2
            print(self.turn)
            board[self.quad][self.row][self.col] = self.piece
            
    def valid_move(self, row, col, quad):
        if self.board[quad][row][col] == 0:
            return True
        else:
            return False
    
    def print_board(self):
        print("   1  2  3      4  5  6")
    
        for i in range(int(len(self.board)/2)):
            print("  -----------------------")
            for j in range(len(self.board[0])):
                if i == 0:
                    print(j + 1, self.board[0][j],"|", self.board[1][j])
                if i ==1:
                    print(j + 1 + len(self.board[0]), self.board[2][j],"|", self.board[3][j])
        print("  -----------------------")       
        
    def rotate_quad(self, board, quad, rotation):
        left = 1
        right = 0
        
        if rotation == left:
            self.board[quad] = list(zip(*reversed(board[quad])))
            self.board[quad] = list(zip(*reversed(board[quad])))
            self.board[quad] = list(zip(*reversed(board[quad])))
        elif rotation == right:
            self.board[quad] = list(zip(*reversed(board[quad])))
            
        return self.board
        
    
    def winning_move(self, board, piece):
        #all horizontal wins
    #     for c in range(col):
        pass
            
    
    def start_game(self):
        self.game_over = False
        self.turn = 0
        while not self.game_over:
            
            #input Player1
            self.print_board()
            if self.turn == 0:
                self.row = int(input("Choose Row (1-6): "))
                self.col = int(input("Choose Column(1-6): "))       
            #input Player2
            else: 
                self.row = int(input("Choose Row (1-6): "))
                self.col = int(input("Choose Column(1-6: "))
                
                
            self.drop_piece(self.row, self.col, self.board)
            
            self.print_board()
            
            self.quad = int(input("What Quadrant do you want to rotate: "))
            self.rotation = int(input("Right(0) or Left(1)"))
            
            self.board = self.rotate_quad(self.board, self.quad - 1, self.rotation)
            
            
           
            
squares = 4
rows = 3 
columns = 3 
pentago = BoardGame(squares, rows, columns)

