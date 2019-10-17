import numpy as np


class BoardGame:
    def __init__(self, squares, row, column):
        self.board = np.zeros((squares,row,column))
        self.start_game()
    def drop_piece(self, row, col, board):
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
            self.turn = self.turn % 2
            board[self.quad][self.row][self.col] = self.piece
            
            if self.winning_move(board, self.piece):
                self.game_over = True
                print(f'Congrats Player {self.turn}, you have won the game!')
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
            
        if self.winning_move(self.board, self.piece):
            self.game_over = True
            print(f'Congrats Player {self.turn}, you have won the game!')
            
        return self.board
        
    
    def winning_move(self, board, piece):
        #horizontal wins
        for i in range(len(board[0]) * 2):
            quad = 0
            row = i
            if i > 2:
                row = i - 3
            col = 0
            if i > 2:
                quad = 2
            if board[quad][row][col] == piece and board[quad][row][col+1] == piece and board[quad][row][col+2] == piece and board[quad + 1][row][col] == piece and board[quad+1][row][col+1] == piece:
                return True
            elif board[quad][row][col+1] == piece and board[quad][row][col+2] == piece and board[quad+1][row][col] == piece and board[quad + 1][row][col+1] == piece and board[quad+1][row][col+2] == piece:
                return True
    
                #vertical win
        for j in range(len(board[0]) * 2):
            quad = 0
            row = 0
            col = j
            if i > 2:
                col = j - 3
            if j > 2:
                quad = 1
            if board[quad][row][col] == piece and board[quad][row+1][col] == piece and board[quad][row+2][col] == piece and board[quad + 2][row][col] == piece and board[quad+2][row+1][col] == piece:
                return True
            elif board[quad][row+1][col] == piece and board[quad][row+2][col] == piece and board[quad+2][row][col] == piece and board[quad + 2][row+1][col] == piece and board[quad+2][row+2][col] == piece:
                return True
        #diagonal wins

        #middle diagonals
        if board[0][0][0] == piece and board[0][1][1] == piece and board[0][2][2] == piece and board[3][0][0] == piece and board[3][1][1] == piece:
            return True
        if board[0][1][1] == piece and board[0][2][2] == piece and board[3][0][0] == piece and board[3][1][1] == piece and board[3][2][2] == piece:
            return True
        if board[2][2][0] == piece and board[2][1][1] == piece and board[2][0][2] == piece and board[1][2][0] == piece and board[1][1][1] == piece:
            return True
        if board[2][1][1] == piece and board[2][0][2] == piece and board[1][2][0] == piece and board[1][1][1] == piece and board[1][0][2] == piece:
            return True
        #side diagonals
        if board[0][1][0] == piece and board[0][2][1] == piece and board[2][0][2]== piece and board[3][1][0] == piece and board[3][2][1] == piece:
            return True
        if board[0][0][1] == piece and board[0][1][2] == piece and board[1][2][0]== piece and board[3][0][1] == piece and board[3][1][2] == piece:
            return True
        if board[1][0][1] == piece and board[1][1][0] == piece and board[0][2][2]== piece and board[2][0][1] == piece and board[2][1][0] == piece:
            return True
        if board[1][1][2] == piece and board[1][2][1] == piece and board[3][0][0]== piece and board[2][1][2] == piece and board[2][2][1] == piece:
            return True
        return False            
    
    def start_game(self):
        self.game_over = False
        self.turn = 0
        while not self.game_over:
            
            #input Player1
            self.print_board()
            if self.turn == 0:
                self.row = int(input("Choose Row (1-6): "))
                assert type(self.row) is int, "% is not an integer" % self.row
                assert self.row <= 6 and self.row >= 1, "Choose a row between 1 and 6"
                self.col = int(input("Choose Column(1-6): "))
                assert type(self.col) is int, "% is not an integer" % self.col
                assert self.col <= 6 and self.col >= 1, "Choose a column between 1 and 6"       
            #input Player2
            else: 
                self.row = int(input("Choose Row (1-6): "))
                assert type(self.row) is int, "% is not an integer" % self.row
                assert self.row <= 6 and self.row >= 1, "Choose a row between 1 and 6"
                self.col = int(input("Choose Column(1-6: "))
                assert type(self.col) is int, "% is not an integer" % self.col
                assert self.col <= 6 and self.col >= 1, "Choose a column between 1 and 6"
                
                
            self.drop_piece(self.row, self.col, self.board)
            
            if self.game_over == True:
                break
            else:
            
                self.print_board()
                
                self.quad = int(input("What Quadrant do you want to rotate: "))
                assert type(self.quad) is int, "% is not an integer" % self.quad
                assert self.quad <= 4 and self.quad >= 1, "Choose quadrant 1, 2, 3, or 4" 
                
                self.rotation = int(input("Right(0) or Left(1): "))
                assert type(self.rotation) is int, "% is not an integer" % self.rotation
                assert self.rotation == 0 or self.rotation == 1, "Choose 0 or 1" 
                
                self.board = self.rotate_quad(self.board, self.quad - 1, self.rotation)
            
            
           
            
squares = 4
rows = 3 
columns = 3 
pentago = BoardGame(squares, rows, columns)

