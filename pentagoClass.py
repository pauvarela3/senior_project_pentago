import numpy as np
import pygame
import sys


#colors used in game
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_RED = (169,0,0)
WHITE = (255,255,255)
GRAY = (131,139,139)
GREEN = (0,255,0)
YELLOW = (0, 127,127)

class Pentago():
    def __init__(self):
        self.squares = 4
        self.rows = 3
        self.columns = 3
        self.board = np.zeros((self.squares, self.rows, self.columns))
        
        self.player1 = False
        self.player2 = False
        self.draw = False
        
        self.turn = 0
        self.state = -1  
    def board_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                for k in range(len(self.board[0][0])):
                    if self.board[i][j][k] == 0:
                        self.draw = True
                        return False
        return True
    def drop_piece(self, row, col):    
        if row > 3 and col > 3:
            quad = 3
            row = row - 4
            col = col - 4
        elif col > 3:
            quad = 1
            col = col - 4
            row = row - 1
        elif row > 3:
            quad = 2
            col = col - 1
            row = row - 4
        else:
            quad = 0
            row = row - 1
            col = col - 1
            
        if self.turn ==0:
            piece = 1
        else:
            piece = 2
            
        new = self.turn + 1
        new = new % 2
            
        if not self.valid_move(row, col, quad):
            print("Space is already occupied, select another place")
            return self.turn
        else:
            self.board[quad][row][col] = piece
            
            if self.winning_move(1):
                self.player1 = True
            if self.winning_move(2):
                self.player2 = True
            if self.player1 and self.player2:
                self.draw = True
                self.state = 3
            elif self.player1 or self.player2:
                print(f'Congrats Player {piece}, you have won the game!')
                self.state = 2
    
            return new
    def valid_move(self, row, col, quad):
        if self.board[quad][row][col] == 0:
            self.state = 1
            return True
        else:
            self.state = 0
            return False
    def winning_move(self, piece):
        #horizontal wins
        for i in range(len(self.board[0]) * 2):
            quad = 0
            row = i
            if i > 2:
                row = i - 3
            col = 0
            if i > 2:
                quad = 2
            if self.board[quad][row][col] == piece and self.board[quad][row][col+1] == piece and self.board[quad][row][col+2] == piece and self.board[quad + 1][row][col] == piece and self.board[quad+1][row][col+1] == piece:
                return True
            elif self.board[quad][row][col+1] == piece and self.board[quad][row][col+2] == piece and self.board[quad+1][row][col] == piece and self.board[quad + 1][row][col+1] == piece and self.board[quad+1][row][col+2] == piece:
                return True
    
                #vertical win
        for j in range(len(self.board[0]) * 2):
            quad = 0
            row = 0
            col = j
            if i > 2:
                col = j - 3
            if j > 2:
                quad = 1
            if self.board[quad][row][col] == piece and self.board[quad][row+1][col] == piece and self.board[quad][row+2][col] == piece and self.board[quad + 2][row][col] == piece and self.board[quad+2][row+1][col] == piece:
                return True
            elif self.board[quad][row+1][col] == piece and self.board[quad][row+2][col] == piece and self.board[quad+2][row][col] == piece and self.board[quad + 2][row+1][col] == piece and self.board[quad+2][row+2][col] == piece:
                return True
            #diagonal wins
    
        #middle diagonals
        if self.board[0][0][0] == piece and self.board[0][1][1] == piece and self.board[0][2][2] == piece and self.board[3][0][0] == piece and self.board[3][1][1] == piece:
            return True
        if self.board[0][1][1] == piece and self.board[0][2][2] == piece and self.board[3][0][0] == piece and self.board[3][1][1] == piece and self.board[3][2][2] == piece:
            return True
        if self.board[2][2][0] == piece and self.board[2][1][1] == piece and self.board[2][0][2] == piece and self.board[1][2][0] == piece and self.board[1][1][1] == piece:
            return True
        if self.board[2][1][1] == piece and self.board[2][0][2] == piece and self.board[1][2][0] == piece and self.board[1][1][1] == piece and self.board[1][0][2] == piece:
            return True
        #side diagonals
        if self.board[0][1][0] == piece and self.board[0][2][1] == piece and self.board[2][0][2]== piece and self.board[3][1][0] == piece and self.board[3][2][1] == piece:
            return True
        if self.board[0][0][1] == piece and self.board[0][1][2] == piece and self.board[1][2][0]== piece and self.board[3][0][1] == piece and self.board[3][1][2] == piece:
            return True
        if self.board[1][0][1] == piece and self.board[1][1][0] == piece and self.board[0][2][2]== piece and self.board[2][0][1] == piece and self.board[2][1][0] == piece:
            return True
        if self.board[1][1][2] == piece and self.board[1][2][1] == piece and self.board[3][0][0]== piece and self.board[2][1][2] == piece and self.board[2][2][1] == piece:
            return True
        return False
    def rotate_quad(self, quad, rotation):
        left = 1
        right = 0
        
        if rotation == left:
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            self.board[quad] = list(zip(*reversed(self.board[quad])))
        elif rotation == right:
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            
        if self.winning_move(1):
            self.player1 = True
            piece = 1
        if self.winning_move(2):
            self.player2 = True
            piece = 2
        if self.player1 and self.player2:
            self.draw = True
            self.state = 3
        elif self.player1 or self.player2:
            print(f'Congrats Player {piece}, you have won the game!')
            self.state = 2
    def clear_board(self):
        self.board = np.zeros((self.squares, self.rows, self.columns))
        self.turn = 0
        self.player1 = False
        self.player2 = False
        self.state = 0

class Board():
    def __init__(self):
        
        #screen and board sizes
        self.indsquare = 90
        self.squaresize = self.indsquare * 3
        self.screensize = self.indsquare * 8
        self.ROW = 6
        self.COL = 6
        
        self.radius = int(self.indsquare/2 - 5)
        
        size = (self.screensize, self.screensize + 65)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Pentago")
        self.default_font = pygame.font.get_default_font()
    def game_menu(self):
        font_gameTitle = pygame.font.Font(self.default_font, 80)
        gameTitle = font_gameTitle.render("PENTAGO", 1, RED)
        self.screen.blit(gameTitle, (165,120))
        coord = (135, 220, 450, 320)
        pygame.draw.rect(self.screen, GRAY, coord)
        button1 = (220, 260, 280, 100)
        pygame.draw.rect(self.screen, BLACK, button1)
        button3 = (220, 400, 280, 100)
        pygame.draw.rect(self.screen, BLACK, button3)
        
        self.font_label = pygame.font.Font(self.default_font, 32)
        self.font_tiny = pygame.font.Font(self.default_font, 20)
        self.font_gameover = pygame.font.Font(self.default_font, 45)
        label1 = self.font_label.render("Start Game:", 1, RED)
        label12 = self.font_tiny.render("One Player", 1, RED)
        label2 = self.font_label.render("Start Game:", 1, RED)
        label22 = self.font_tiny.render("Two Player", 1, RED)
        
        self.screen.blit(label1, (265, 280))
        self.screen.blit(label12, (300, 310))
        self.screen.blit(label2, (265, 420))
        self.screen.blit(label22, (300, 450))
                
        pygame.display.update()   
    def gamemenuButton(self, x,y):
        if( 219 < x and x < 501) and (259 < y and y < 359):
            return 0
        
        elif (219 < x and x < 501) and (399 < y and y < 501):
            return 1
        else:
            return -1
    def draw_board(self, board, turn):
        
        pygame.draw.rect(self.screen, BLACK, (65, 65, (self.squaresize * 2) + 45, (self.squaresize * 2) + 45))
        label = self.font_gameover.render(f"Game Over:  Player {turn + 1} Won!", 1, BLACK, BLACK)
        self.screen.blit(label, (65,340))
        label = self.font_label.render(f"Turn: Player {turn + 1}", 1, WHITE, BLACK)
        self.screen.blit(label, (245,670))
        label = self.font_label.render("  Start Over  ", 1, WHITE, GRAY)
        self.screen.blit(label, (65, 710))

        
        pygame.draw.rect(self.screen, RED, (65,65,self.squaresize, self.squaresize), 2)
        for c in range(3):
            for r in range(3):
                pygame.draw.rect(self.screen,RED, ((c*self.indsquare)+65, (r*self.indsquare)+65, self.indsquare, self.indsquare))
                
                if board[0][r][c] == 0:
                    pygame.draw.circle(self.screen,DARK_RED, (int(c*self.indsquare+(self.indsquare/2))+65, int(r*self.indsquare+(self.indsquare/2))+65), self.radius)
                if board[0][r][c] == 1:
                    pygame.draw.circle(self.screen,WHITE, (int(c*self.indsquare+(self.indsquare/2))+65, int(r*self.indsquare+(self.indsquare/2))+65), self.radius)
                if board[0][r][c] == 2:
                    pygame.draw.circle(self.screen,BLACK, (int(c*self.indsquare+(self.indsquare/2))+65, int(r*self.indsquare+(self.indsquare/2))+65), self.radius)
    
    
        pygame.draw.rect(self.screen, RED, (self.squaresize + 110, 65, self.squaresize, self.squaresize), 2)
        for c in range(3):
            for r in range(3):
                pygame.draw.rect(self.screen,RED, ((c*self.indsquare)+110 + self.squaresize, (r*self.indsquare)+65, self.indsquare, self.indsquare))
                
                if board[1][r][c] == 0:
                    pygame.draw.circle(self.screen,DARK_RED, (int(c*self.indsquare+(self.indsquare/2))+380, int(r*self.indsquare+(self.indsquare/2))+65), self.radius)
                if board[1][r][c] == 1:
                    pygame.draw.circle(self.screen,WHITE, (int(c*self.indsquare+(self.indsquare/2))+380, int(r*self.indsquare+(self.indsquare/2))+65), self.radius)
                if board[1][r][c] == 2:
                    pygame.draw.circle(self.screen,BLACK, (int(c*self.indsquare+(self.indsquare/2))+380, int(r*self.indsquare+(self.indsquare/2))+65), self.radius)
    
        pygame.draw.rect(self.screen, RED, (65, 110 + self.squaresize, self.squaresize, self.squaresize), 2)
        for c in range(3):
            for r in range(3):
                pygame.draw.rect(self.screen,RED, ((c*self.indsquare)+65, (r*self.indsquare)+110 + self.squaresize, self.indsquare, self.indsquare))
                
                if board[2][r][c] == 0:
                    pygame.draw.circle(self.screen,DARK_RED, (int(c*self.indsquare+(self.indsquare/2))+65, int(r*self.indsquare+(self.indsquare/2))+380), self.radius)
                if board[2][r][c] == 1:
                    pygame.draw.circle(self.screen,WHITE, (int(c*self.indsquare+(self.indsquare/2))+65, int(r*self.indsquare+(self.indsquare/2))+380), self.radius)
                if board[2][r][c] == 2:
                    pygame.draw.circle(self.screen,BLACK, (int(c*self.indsquare+(self.indsquare/2))+65, int(r*self.indsquare+(self.indsquare/2))+380), self.radius)
    
        pygame.draw.rect(self.screen, RED, (self.squaresize + 110, 110 + self.squaresize, self.squaresize, self.squaresize), 2)
        for c in range(3):
            for r in range(3):
                pygame.draw.rect(self.screen,RED, ((c*self.indsquare)+110 +self.squaresize, (r*self.indsquare)+110 + self.squaresize, self.indsquare, self.indsquare))
                
                if board[3][r][c] == 0:
                    pygame.draw.circle(self.screen,DARK_RED, (int(c*self.indsquare+(self.indsquare/2))+380, int(r*self.indsquare+(self.indsquare/2))+380), self.radius)
                if board[3][r][c] == 1:
                    pygame.draw.circle(self.screen,WHITE, (int(c*self.indsquare+(self.indsquare/2))+380, int(r*self.indsquare+(self.indsquare/2))+380), self.radius)
                if board[3][r][c] == 2:
                    pygame.draw.circle(self.screen,BLACK, (int(c*self.indsquare+(self.indsquare/2))+380, int(r*self.indsquare+(self.indsquare/2))+380), self.radius)
    def draw_arrows(self, color):
        x = 15
        y = 70
        pygame.draw.polygon(self.screen, color, ((16+x,10+y),(16+x,50+y),(8+x,50+y),(23+x,75+y),(38+x,50+y),(30+x,50+y),(30+x,10+y)))
         
        x = 655
        y = 70 
        pygame.draw.polygon(self.screen, color, ((16+x,10+y),(16+x,50+y),(8+x,50+y),(23+x,75+y),(38+x,50+y),(30+x,50+y),(30+x,10+y)))
        
        x = 70
        y = 15
        pygame.draw.polygon(self.screen, color, ((10+x,16+y),(50+x,16+y),(50+x,8+y),(75+x,23+y),(50+x,38+y),(50+x,30+y),(10+x,30+y)))
                            
        x = 70
        y = 655
        pygame.draw.polygon(self.screen, color, ((10+x,16+y),(50+x,16+y),(50+x,8+y),(75+x,23+y),(50+x,38+y),(50+x,30+y),(10+x,30+y)))
    
        x = 655
        y = 570
        pygame.draw.polygon(self.screen, color, ((16+x,75+y),(16+x,35+y),(8+x,35+y),(23+x,10+y),(38+x, 35+y),(30+x,35+y),(30+x,75+y)))
    
        x = 15
        y = 570
        pygame.draw.polygon(self.screen, color, ((16+x,75+y),(16+x,35+y),(8+x,35+y),(23+x,10+y),(38+x,35+y),(30+x,35+y),(30+x,75+y)))
    
    
        x = 570
        y = 15
        pygame.draw.polygon(self.screen, color, ((10+x,23+y),(35+x,8+y),(35+x,16+y),(75+x,16+y),(75+x,30+y),(35+x,30+y),(35+x,38+y)))
        
        x = 570
        y = 655
        pygame.draw.polygon(self.screen, color, ((10+x,23+y),(35+x,8+y),(35+x,16+y),(75+x,16+y),(75+x,30+y),(35+x,30+y),(35+x,38+y)))
    def whichQuadRot(self, x,y):
        if (80 < x and x < 145) and (23 < y and y < 45): 
            quad = 0
            rotation = 0
        elif (23 < x and x < 53) and (80 < y and y < 145):
            quad=0
            rotation=1
        elif (663 < x and x < 693) and (80 < y and y < 145):
            quad=1
            rotation=0
        elif (580 < x and x < 645) and (23 < y and y < 53): 
            quad = 1
            rotation= 1
        elif (23 < x and x < 53) and (580 < y and y < 645):
            quad = 2
            rotation = 0
        elif (80 < x and x < 145) and (663 < y and y < 693):
            quad = 2
            rotation = 1
        elif (663 < x and x < 693) and (580 < y and y < 645):
            quad = 3
            rotation = 1
        elif (580 < x and x < 645) and (663 < y and y < 693):
            quad = 3
            rotation = 0
        else:
            quad = 5
            rotation = 5
        return quad, rotation
    def whichRowCol(self, value):
        if value > 70 and value < 150:
            x = 1
        elif value > 160 and value < 238:
            x = 2
        elif value > 249 and value < 329:
            x = 3
        elif value > 386 and value < 463:
            x = 4
        elif value > 476 and value < 554:
            x = 5
        elif value > 566 and value < 644:
            x = 6
        else: 
            x = 0
        
        return x 
        
#Game Running
    def clearButton(self, x,y):
        if(x > 65 and x <223) and (y > 713 and y < 744):
            return True  
        else:
            return False 
def running():
    running = True
    
    pygame.init()

    pentago = Pentago()
    board = Board()
    moveComplete = False
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and board.clearButton(event.pos[0],event.pos[1]):
                pentago.clear_board()
                board.draw_board(pentago.board, pentago.turn)
                board.draw_arrows(BLACK)
                pygame.display.update()
                
            elif pentago.board_full() and moveComplete:
                pentago.state = 3 
            
            elif pentago.state == -1:
                #start menu
                board.game_menu()
                pygame.display.update()
                
                pressed = 2
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = board.gamemenuButton(event.pos[0], event.pos[1])
                
                if pressed == 0: #one player
                    pentago.state = 0
                if pressed == 1: #two player
                    pentago.state = 0
                else:
                    pass
            elif pentago.state == 2:
#               game won by one player
                if pentago.player1:
                    label = board.font_gameover.render(f"Game Over:  Player 1 Won!", 1, RED, BLACK)
                    board.screen.blit(label, (65,340))
                    pygame.display.update()
                if pentago.player2:
                    label = board.font_gameover.render(f"Game Over:  Player 2 Won!", 1, RED, BLACK)
                    board.screen.blit(label, (65,340))
                    pygame.display.update()
                pentago.state = 2
            elif pentago.state == 3:
#               game draw
                if pentago.draw:
                    label = board.font_gameover.render(f"Game Over: Draw", 1, RED, BLACK)
                    board.screen.blit(label, (65,340))
                    pygame.display.update()
                pentago.state = 3
                
            else:
                board.draw_board(pentago.board, pentago.turn)
                pygame.display.update()
                if pentago.state == 0:
                    #drop piece
                    moveComplete = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x = event.pos[0]
                        y = event.pos[1]
                            
                        col = board.whichRowCol(x)
                        row = board.whichRowCol(y)
                        if col == 0 or row == 0:
                            continue
                        else:
                            if pentago.turn == 0:
                                new = pentago.drop_piece(row, col)
                            else:
                                new = pentago.drop_piece(row, col)
                            
                        board.draw_board(pentago.board, pentago.turn)
                        pygame.display.update()
                    
                        
                if pentago.state == 1:
                    #rotate quadrant
                    board.draw_arrows(GRAY)
                    pygame.display.update()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x = event.pos[0]
                        y = event.pos[1]
                        
                        quad, rotation = board.whichQuadRot(x,y)
                        if quad == 5 or rotation == 5:
                            pass
                        else:
                            pentago.rotate_quad(quad, rotation)
                            board.draw_board(pentago.board, pentago.turn)
                            pygame.display.update()
                            
                            moveComplete = True

                            pentago.turn = new
                            
                            print(pentago.turn)
                            if pentago.state == 0 or pentago.state == 1:
                                pentago.state += 1
                                pentago.state = pentago.state % 2
                                print(pentago.state)
                        board.draw_arrows(BLACK)
                        board.draw_board(pentago.board, pentago.turn)
                        pygame.display.update()

running()        
        