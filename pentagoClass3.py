# AI is Player 1 with both buttons

# MAIN PENTAGO

# BUGS
# HUMAN (player 1) vs AI.  Human starts as 'Turn 2'
# HUMAN VS HUMAN not recognizing draw on full board.  Draws on rotation recognized.  Not sure for all play options
# HUMAN VS HUMAN.  If game restarted, AI plays as player 1



import numpy as np
import random
import time
import pygame
import sys
import AI
import AI_Defense
import BoardHash

new = time.localtime(time.time())
random.seed(new)

print("this is main code")

#colors used in game
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_RED = (169,0,0)
WHITE = (255,255,255)
GRAY = (131,139,139)
GREEN = (0,255,0)
YELLOW = (0, 127,127)

# variables for positioning 'game over' message
gameOver_dimension_x = 100
gameOver_dimension_y = 645
gameOver_font = 40

# variables for positioning 'player turn' message
playerTurn_dimension_x = 245
playerTurn_dimension_y = 645



# variables for positioning arrows
arrow_align_top = 35
arrow_align_bottom = 640
arrow_align_left = 30
arrow_align_right = 640








#GLOBALS ADDED BY GEORGE
quad_0_rotation = 0
quad_1_rotation = 0
quad_2_rotation = 0
quad_3_rotation = 0


class Pentago():
    def __init__(self):
        self.squares = 4
        self.rows = 3
        self.columns = 3
        self.board = np.zeros((self.squares, self.rows, self.columns))

        self.player1 = False
        self.player2 = False
        self.twoplayer = False
        self.humanfirst = False
        self.draw = False

        self.turn = 0
        self.state = -1
        self.moves = np.zeros((36,6))
        self.top = -1
    def board_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                for k in range(len(self.board[0][0])):
                    if self.board[i][j][k] == 0:
                        self.draw = True
                        return False
        return True
    def drop_piece(self, row, col):
        global quad_0_rotation
        global quad_1_rotation
        global quad_2_rotation
        global quad_3_rotation
        if row > 3 and col > 3:
            quad = 3
            row = row - 4
            col = col - 4
            #Here, I'm changing which variable is in which spot
            #based on the rotations of the quad :)
            #These first 4 if statements are for quad_3
            if quad_3_rotation == 0:
                if col == 0:
                    if row == 0:
                        variable_number = 21
                    elif row == 1:
                        variable_number = 27
                    else:
                        variable_number = 33
                elif col == 1:
                    if row == 0:
                        variable_number = 22
                    elif row == 1:
                        variable_number = 28
                    else:
                        variable_number = 34
                else:
                    if row == 0:
                        variable_number = 23
                    elif row == 1:
                        variable_number = 29
                    else:
                        variable_number = 35
    ###############################################################################
            elif quad_3_rotation == 1:
                if col == 0:
                    if row == 0:
                        variable_number = 33
                    elif row == 1:
                        variable_number = 34
                    else:
                        variable_number = 35
                elif col == 1:
                    if row == 0:
                        variable_number = 27
                    elif row == 1:
                        variable_number = 28
                    else:
                        variable_number = 29
                else:
                    if row == 0:
                        variable_number = 21
                    elif row == 1:
                        variable_number = 22
                    else:
                        variable_number = 23
    ################################################################################
            elif quad_3_rotation == 2:
                if col == 0:
                    if row == 0:
                        variable_number = 35
                    elif row == 1:
                        variable_number = 29
                    else:
                        variable_number = 23
                elif col == 1:
                    if row == 0:
                        variable_number = 34
                    elif row == 1:
                        variable_number = 28
                    else:
                        variable_number = 22
                else:
                    if row == 0:
                        variable_number = 33
                    elif row == 1:
                        variable_number = 27
                    else:
                        variable_number = 21
    ################################################################################
            elif quad_3_rotation == 3:
                if col == 0:
                    if row == 0:
                        variable_number = 23
                    elif row == 1:
                        variable_number = 22
                    else:
                        variable_number = 21
                elif col == 1:
                    if row == 0:
                        variable_number = 29
                    elif row == 1:
                        variable_number = 28
                    else:
                        variable_number = 27
                else:
                    if row == 0:
                        variable_number = 35
                    elif row == 1:
                        variable_number = 34
                    else:
                        variable_number = 33
#///////////////////////////////////////////////////////////////////////////////
        elif col > 3:
            quad = 1
            col = col - 4
            row = row - 1
            if quad_1_rotation == 0:
                if col == 0:
                    if row == 0:
                        variable_number = 3
                    elif row == 1:
                        variable_number = 9
                    else:
                        variable_number = 15
                elif col == 1:
                    if row == 0:
                        variable_number = 4
                    elif row == 1:
                        variable_number = 10
                    else:
                        variable_number = 16
                else:
                    if row == 0:
                        variable_number = 5
                    elif row == 1:
                        variable_number = 11
                    else:
                        variable_number = 17
    ################################################################################
            elif quad_1_rotation == 1:
                if col == 0:
                    if row == 0:
                        variable_number = 15
                    elif row == 1:
                        variable_number = 16
                    else:
                        variable_number = 17
                elif col == 1:
                    if row == 0:
                        variable_number = 9
                    elif row == 1:
                        variable_number = 10
                    else:
                        variable_number = 11
                else:
                    if row == 0:
                        variable_number = 3
                    elif row == 1:
                        variable_number = 4
                    else:
                        variable_number = 5
    ################################################################################
            elif quad_1_rotation == 2:
                if col == 0:
                    if row == 0:
                        variable_number = 17
                    elif row == 1:
                        variable_number = 11
                    else:
                        variable_number = 5
                elif col == 1:
                    if row == 0:
                        variable_number = 16
                    elif row == 1:
                        variable_number = 10
                    else:
                        variable_number = 4
                else:
                    if row == 0:
                        variable_number = 15
                    elif row == 1:
                        variable_number = 9
                    else:
                        variable_number = 3
    #################################################################################
            elif quad_1_rotation == 3:
                if col == 0:
                    if row == 0:
                        variable_number = 5
                    elif row == 1:
                        variable_number = 4
                    else:
                        variable_number = 3
                elif col == 1:
                    if row == 0:
                        variable_number = 11
                    elif row == 1:
                        variable_number = 10
                    else:
                        variable_number = 9
                else:
                    if row == 0:
                        variable_number = 17
                    elif row == 1:
                        variable_number = 16
                    else:
                        variable_number = 15
#////////////////////////////////////////////////////////////////////////////////
        elif row > 3:
            quad = 2
            col = col - 1
            row = row - 4
            if quad_2_rotation == 0:
                if col == 0:
                    if row == 0:
                        variable_number = 18
                    elif row == 1:
                        variable_number = 24
                    else:
                        variable_number = 30
                elif col == 1:
                    if row == 0:
                        variable_number = 19
                    elif row == 1:
                        variable_number = 25
                    else:
                        variable_number = 31
                else:
                    if row == 0:
                        variable_number = 20
                    elif row == 1:
                        variable_number = 26
                    else:
                        variable_number = 32
    ##################################################################################
            elif quad_2_rotation == 1:
                if col == 0:
                    if row == 0:
                        variable_number = 30
                    elif row == 1:
                        variable_number = 31
                    else:
                        variable_number = 32
                elif col == 1:
                    if row == 0:
                        variable_number = 24
                    elif row == 1:
                        variable_number = 25
                    else:
                        variable_number = 26
                else:
                    if row == 0:
                        variable_number = 18
                    elif row == 1:
                        variable_number = 19
                    else:
                        variable_number = 20
    ##################################################################################
            elif quad_2_rotation == 2:
                if col == 0:
                    if row == 0:
                        variable_number = 32
                    elif row == 1:
                        variable_number = 26
                    else:
                        variable_number = 20
                elif col == 1:
                    if row == 0:
                        variable_number = 31
                    elif row == 1:
                        variable_number = 25
                    else:
                        variable_number = 19
                else:
                    if row == 0:
                        variable_number = 30
                    elif row == 1:
                        variable_number = 24
                    else:
                        variable_number = 18
    ##################################################################################
            elif quad_2_rotation == 3:
                if col == 0:
                    if row == 0:
                        variable_number = 20
                    elif row == 1:
                        variable_number = 19
                    else:
                        variable_number = 18
                elif col == 1:
                    if row == 0:
                        variable_number = 26
                    elif row == 1:
                        variable_number = 25
                    else:
                        variable_number = 24
                else:
                    if row == 0:
                        variable_number = 32
                    elif row == 1:
                        variable_number = 31
                    else:
                        variable_number = 30
#////////////////////////////////////////////////////////////////////////////////
        else:
            quad = 0
            row = row - 1
            col = col - 1
            if quad_0_rotation == 0:
                if col == 0:
                    if row == 0:
                        variable_number = 0
                    elif row == 1:
                        variable_number = 6
                    else:
                        variable_number = 12
                elif col == 1:
                    if row == 0:
                        variable_number = 1
                    elif row == 1:
                        variable_number = 7
                    else:
                        variable_number = 13
                else:
                    if row == 0:
                        variable_number = 2
                    elif row == 1:
                        variable_number = 8
                    else:
                        variable_number = 14
    ##################################################################################
            elif quad_0_rotation == 1:
                if col == 0:
                    if row == 0:
                        variable_number = 12
                    elif row == 1:
                        variable_number = 13
                    else:
                        variable_number = 14
                elif col == 1:
                    if row == 0:
                        variable_number = 6
                    elif row == 1:
                        variable_number = 7
                    else:
                        variable_number = 8
                else:
                    if row == 0:
                        variable_number = 0
                    elif row == 1:
                        variable_number = 1
                    else:
                        variable_number = 2
    ##################################################################################
            elif quad_0_rotation == 2:
                if col == 0:
                    if row == 0:
                        variable_number = 14
                    elif row == 1:
                        variable_number = 8
                    else:
                        variable_number = 2
                elif col == 1:
                    if row == 0:
                        variable_number = 13
                    elif row == 1:
                        variable_number = 7
                    else:
                        variable_number = 1
                else:
                    if row == 0:
                        variable_number = 12
                    elif row == 1:
                        variable_number = 6
                    else:
                        variable_number = 0
    ##################################################################################
            elif quad_0_rotation == 3:
                if col == 0:
                    if row == 0:
                        variable_number = 2
                    elif row == 1:
                        variable_number = 1
                    else:
                        variable_number = 0
                elif col == 1:
                    if row == 0:
                        variable_number = 8
                    elif row == 1:
                        variable_number = 7
                    else:
                        variable_number = 6
                else:
                    if row == 0:
                        variable_number = 14
                    elif row == 1:
                        variable_number = 13
                    else:
                        variable_number = 12
        AI.score_taking(variable_number,self.turn)
        AI_Defense.score_taking(variable_number,self.turn)
        if self.turn ==0:
            piece = 1
        else:
            piece = 2

        #new = self.turn + 1
        #new = new % 2

        if not self.valid_move(row, col, quad):
            #maybe put a label here
            # print("Space is already occupied, select another place")
            return self.turn
        else:
            ## for undo button, not necessary
            self.board[quad][row][col] = piece
            self.top += 1
            self.moves[self.top][0] = self.turn + 1
            self.moves[self.top][1] = quad
            self.moves[self.top][2] = row
            self.moves[self.top][3] = col
            ## undo ends here

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
        global quad_0_rotation
        global quad_1_rotation
        global quad_2_rotation
        global quad_3_rotation
        left = 1
        right = 0
        ## undo button , not necessary
        self.moves[self.top][4] = quad
        self.moves[self.top][5] = rotation
        ## undo ends here
        #GEORGE STUFF

        #In here, I ended up adding code to make sure
        #That the quad_#_rotation get updated based on
        #which rotation was done.
        if rotation == left:
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            if quad == 0:
                quad_0_rotation = quad_0_rotation - 1
            elif quad == 1:
                quad_1_rotation = quad_1_rotation - 1
            elif quad == 2:
                quad_2_rotation = quad_2_rotation - 1
            else:
                quad_3_rotation = quad_3_rotation - 1
        elif rotation == right:
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            if quad == 0:
                quad_0_rotation = quad_0_rotation + 1
            elif quad == 1:
                quad_1_rotation = quad_1_rotation + 1
            elif quad == 2:
                quad_2_rotation = quad_2_rotation + 1
            else:
                quad_3_rotation = quad_3_rotation + 1
        if quad_0_rotation == 4:
            quad_0_rotation = 0
        elif quad_0_rotation == -1:
            quad_0_rotation = 3
        if quad_1_rotation == 4:
            quad_1_rotation = 0
        elif quad_1_rotation == -1:
            quad_1_rotation = 3
        if quad_2_rotation == 4:
            quad_2_rotation = 0
        elif quad_2_rotation == -1:
            quad_2_rotation = 3
        if quad_3_rotation == 4:
            quad_3_rotation = 0
        elif quad_3_rotation == -1:
            quad_3_rotation = 3
        #AI stuff to update scores based on the rotations
        AI.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation)
        AI_Defense.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation)

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
            # print(f'Congrats Player {piece}, you have won the game!')
            self.state = 2
    def clear_board(self, setting):
        global quad_0_rotation
        global quad_1_rotation
        global quad_2_rotation
        global quad_3_rotation
        self.board = np.zeros((self.squares, self.rows, self.columns))
        self.turn = 0
        self.player1 = False
        self.player2 = False
        self.twoplayer = False
        if setting == "menu":
            self.state = -1
        elif setting == "reset":
            self.state = 0
            if self.humanfirst == True:
                self.turn = 1
        else:
            self.state = 0
        self.moves = np.zeros((36,6))
        self.top = -1
        AI.reset_board()
        AI_Defense.reset_board()
        quad_0_rotation = 0
        quad_1_rotation = 0
        quad_2_rotation = 0
        quad_3_rotation = 0

    def undo(self):
        #not fully working with ai but works with two player
        if self.top == -1:
            return

        quad = int(self.moves[self.top][4])
        rotation = int(self.moves[self.top][5])

        left = 1
        right = 0

        if rotation == left:
            self.board[quad] = list(zip(*reversed(self.board[quad])))
        if rotation == right:
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            self.board[quad] = list(zip(*reversed(self.board[quad])))
            self.board[quad] = list(zip(*reversed(self.board[quad])))

        row = int(self.moves[self.top][2])
        col = int(self.moves[self.top][3])
        movequad = int(self.moves[self.top][4])
        self.board[movequad][row][col] = 0
        for x in range(len(self.moves[self.top])):
            self.moves[self.top][x] = 0
        self.top -= 1

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
        pygame.draw.rect(self.screen, BLACK, (0,0, self.screensize, self.screensize + 65))
        font_gameTitle = pygame.font.Font(self.default_font, 80)
        gameTitle = font_gameTitle.render("PENTAGO", 1, RED)
        self.screen.blit(gameTitle, (165,120))
        coord = (135, 220, 450, 320)
        pygame.draw.rect(self.screen, GRAY, coord)
        button1 = (225, 300, 270, 64)
        pygame.draw.rect(self.screen, BLACK, button1)
        button2 = (225, 380, 270, 64)
        pygame.draw.rect(self.screen, BLACK, button2)
        button3 = (225, 460, 270, 64)
        pygame.draw.rect(self.screen, BLACK, button3)

        self.font_label = pygame.font.Font(self.default_font, 32)
        self.font_tiny = pygame.font.Font(self.default_font, 20)
        self.font_gameover = pygame.font.Font(self.default_font, gameOver_font)
        label1 = self.font_label.render("SELECT GAME", 1, RED)
        label12 = self.font_tiny.render("Human vs. AI", 1, RED)
        label12_2 = self.font_tiny.render("Player 1", 1, RED)
        label22 = self.font_tiny.render("Human vs. AI", 1, RED)
        label22_2 = self.font_tiny.render("Player 2", 1, RED)
        label32 = self.font_tiny.render("Human vs. Human", 1, RED)

        self.screen.blit(label1, (242, 250))
        self.screen.blit(label12, (290, 312))
        self.screen.blit(label12_2, (315, 338))
        self.screen.blit(label22, (290, 392))
        self.screen.blit(label22_2, (315, 418))
        self.screen.blit(label32, (270, 480))

        pygame.display.update()
    def gamemenuButton(self, x,y):
        if( 225 < x and x < 495) and (300 < y and y < 364):
            return 0

        elif (225 < x and x < 495) and (380 < y and y < 444):
            return 1
        elif (225 < x < 495) and (460 < y < 524):
            return 2
        else:
            return -1
    def draw_board(self, board, turn):


        pygame.draw.rect(self.screen, BLACK, (65, 65, (self.squaresize * 2) + 45, (self.squaresize * 2) + 45))
        label = self.font_gameover.render(f"Game Over:  Player {turn + 1} Won!", 1, BLACK, BLACK)
        self.screen.blit(label, (gameOver_dimension_x, gameOver_dimension_y))
        label = self.font_label.render(f"Turn: Player {turn + 1}", 1, WHITE, BLACK)
        self.screen.blit(label, (playerTurn_dimension_x, playerTurn_dimension_y))
        label = self.font_label.render("  Restart  ", 1, WHITE, GRAY)
        self.screen.blit(label, (85, 710))
        label = self.font_label.render("   Menu   ", 1, WHITE, GRAY)
        self.screen.blit(label, (500, 710))

        # top left quadrant
        pygame.draw.rect(self.screen, RED, (85,85,self.squaresize, self.squaresize), 2)
        for c in range(3):
            for r in range(3):
                pygame.draw.rect(self.screen,RED, ((c*self.indsquare)+85, (r*self.indsquare)+85, self.indsquare, self.indsquare))

                if board[0][r][c] == 0:
                    pygame.draw.circle(self.screen,DARK_RED, (int(c*self.indsquare+(self.indsquare/2))+85, int(r*self.indsquare+(self.indsquare/2))+85), self.radius)
                if board[0][r][c] == 1:
                    pygame.draw.circle(self.screen,WHITE, (int(c*self.indsquare+(self.indsquare/2))+85, int(r*self.indsquare+(self.indsquare/2))+85), self.radius)
                if board[0][r][c] == 2:
                    pygame.draw.circle(self.screen,BLACK, (int(c*self.indsquare+(self.indsquare/2))+85, int(r*self.indsquare+(self.indsquare/2))+85), self.radius)

        # top right quadrant
        pygame.draw.rect(self.screen, RED, (self.squaresize + 95, 85, self.squaresize, self.squaresize), 2)
        for c in range(3):
            for r in range(3):
                pygame.draw.rect(self.screen,RED, ((c*self.indsquare)+95 + self.squaresize, (r*self.indsquare)+85, self.indsquare, self.indsquare))

                if board[1][r][c] == 0:
                    pygame.draw.circle(self.screen,DARK_RED, (int(c*self.indsquare+(self.indsquare/2))+365, int(r*self.indsquare+(self.indsquare/2))+85), self.radius)
                if board[1][r][c] == 1:
                    pygame.draw.circle(self.screen,WHITE, (int(c*self.indsquare+(self.indsquare/2))+365, int(r*self.indsquare+(self.indsquare/2))+85), self.radius)
                if board[1][r][c] == 2:
                    pygame.draw.circle(self.screen,BLACK, (int(c*self.indsquare+(self.indsquare/2))+365, int(r*self.indsquare+(self.indsquare/2))+85), self.radius)

        # bottom left quadrant
        pygame.draw.rect(self.screen, RED, (85, 95 + self.squaresize, self.squaresize, self.squaresize), 2)
        for c in range(3):
            for r in range(3):
                pygame.draw.rect(self.screen,RED, ((c*self.indsquare)+85, (r*self.indsquare)+95 + self.squaresize, self.indsquare, self.indsquare))

                if board[2][r][c] == 0:
                    pygame.draw.circle(self.screen,DARK_RED, (int(c*self.indsquare+(self.indsquare/2))+85, int(r*self.indsquare+(self.indsquare/2))+365), self.radius)
                if board[2][r][c] == 1:
                    pygame.draw.circle(self.screen,WHITE, (int(c*self.indsquare+(self.indsquare/2))+85, int(r*self.indsquare+(self.indsquare/2))+365), self.radius)
                if board[2][r][c] == 2:
                    pygame.draw.circle(self.screen,BLACK, (int(c*self.indsquare+(self.indsquare/2))+85, int(r*self.indsquare+(self.indsquare/2))+365), self.radius)

        # bottom right quadrant
        pygame.draw.rect(self.screen, RED, (self.squaresize + 95, 95 + self.squaresize, self.squaresize, self.squaresize), 2)
        for c in range(3):
            for r in range(3):
                pygame.draw.rect(self.screen,RED, ((c*self.indsquare)+95 +self.squaresize, (r*self.indsquare)+95 + self.squaresize, self.indsquare, self.indsquare))

                if board[3][r][c] == 0:
                    pygame.draw.circle(self.screen,DARK_RED, (int(c*self.indsquare+(self.indsquare/2))+365, int(r*self.indsquare+(self.indsquare/2))+365), self.radius)
                if board[3][r][c] == 1:
                    pygame.draw.circle(self.screen,WHITE, (int(c*self.indsquare+(self.indsquare/2))+365, int(r*self.indsquare+(self.indsquare/2))+365), self.radius)
                if board[3][r][c] == 2:
                    pygame.draw.circle(self.screen,BLACK, (int(c*self.indsquare+(self.indsquare/2))+365, int(r*self.indsquare+(self.indsquare/2))+365), self.radius)

    def draw_arrows(self, color):
        # top_left__down
        x = arrow_align_left
        y = 70
        pygame.draw.polygon(self.screen, color, (
        (16 + x, 10 + y), (16 + x, 50 + y), (8 + x, 50 + y), (23 + x, 75 + y), (38 + x, 50 + y), (30 + x, 50 + y),
        (30 + x, 10 + y)))

        # top_right__down
        x = arrow_align_right
        y = 70
        pygame.draw.polygon(self.screen, color, (
        (16 + x, 10 + y), (16 + x, 50 + y), (8 + x, 50 + y), (23 + x, 75 + y), (38 + x, 50 + y), (30 + x, 50 + y),
        (30 + x, 10 + y)))

        # top_left_right
        x = 70
        y = arrow_align_top
        pygame.draw.polygon(self.screen, color, (
        (10 + x, 16 + y), (50 + x, 16 + y), (50 + x, 8 + y), (75 + x, 23 + y), (50 + x, 38 + y), (50 + x, 30 + y),
        (10 + x, 30 + y)))

        # top_right_left
        x = 570
        y = arrow_align_top
        pygame.draw.polygon(self.screen, color, (
            (10 + x, 23 + y), (35 + x, 8 + y), (35 + x, 16 + y), (75 + x, 16 + y), (75 + x, 30 + y), (35 + x, 30 + y),
            (35 + x, 38 + y)))

        # bottom_left_right
        x = 70
        y = arrow_align_bottom
        pygame.draw.polygon(self.screen, color, (
        (10 + x, 16 + y), (50 + x, 16 + y), (50 + x, 8 + y), (75 + x, 23 + y), (50 + x, 38 + y), (50 + x, 30 + y),
        (10 + x, 30 + y)))

        # bottom_right_up
        x = arrow_align_right
        y = 570
        pygame.draw.polygon(self.screen, color, (
        (16 + x, 75 + y), (16 + x, 35 + y), (8 + x, 35 + y), (23 + x, 10 + y), (38 + x, 35 + y), (30 + x, 35 + y),
        (30 + x, 75 + y)))

        # bottom_left_up
        x = arrow_align_left
        y = 570
        pygame.draw.polygon(self.screen, color, (
        (16 + x, 75 + y), (16 + x, 35 + y), (8 + x, 35 + y), (23 + x, 10 + y), (38 + x, 35 + y), (30 + x, 35 + y),
        (30 + x, 75 + y)))

        # bottom_right_left
        x = 570
        y = arrow_align_bottom
        pygame.draw.polygon(self.screen, color, (
        (10 + x, 23 + y), (35 + x, 8 + y), (35 + x, 16 + y), (75 + x, 16 + y), (75 + x, 30 + y), (35 + x, 30 + y),
        (35 + x, 38 + y)))

    def whichQuadRot(self, x, y):
        if (80 < x < 145) and (37 < y < 67):
            # print(f'y: {y}')
            # print(f'x: {x}')
            quad = 0
            rotation = 0
            # print("one")
        elif (38 < x < 68) and (80 < y < 145):
            # print(f'y: {y}')
            # print(f'x: {x}')
            quad = 0
            rotation = 1
            # print("two")
        elif (650 < x < 693) and (80 < y < 145):
            # print(f'y: {y}')
            # print(f'x: {x}')
            quad = 1
            rotation = 0
            # print("three")
        elif (580 < x < 645) and (37 < y < 67):
            # print(f'y: {y}')
            # print(f'x: {x}')
            quad = 1
            rotation = 1
            # print("four")
        elif (38 < x < 68) and (580 < y < 645):
            # print(f'y: {y}')
            # print(f'x: {x}')
            quad = 2
            rotation = 0
            # print("five")
        elif (80 < x < 145) and (650 < y < 693):
            # print(f'y: {y}')
            # print(f'x: {x}')
            quad = 2
            rotation = 1
            # print("six")
        elif (650 < x < 693) and (580 < y < 645):
            # print(f'y: {y}')
            # print(f'x: {x}')
            quad = 3
            rotation = 1
            # print("seven")
        elif (580 < x < 645) and (650 < y < 693):
            # print(f'y: {y}')
            # print(f'x: {x}')
            quad = 3
            rotation = 0
            # print("eight")
        else:
            quad = 5
            rotation = 5
            # print("none")
        return quad, rotation

        # circle code

    def whichRowCol(self, value):
        if 90 < value < 170:
            x = 1
            # print("1 circle")
        elif 180 < value < 260:
            x = 2
            # print("2 circle ")
        elif 270 < value < 350:
            x = 3
            # print("3 circle ")
        elif 370 < value < 450:
            x = 4
            # print("4 circle ")
        elif 460 < value < 540:
            x = 5
            # print("5 circle ")
        elif 550 < value < 630:
            x = 6
            # print("6 circle ")
        else:
            x = 0
            # print("out of range")

        # print(f'x value for circle: {x}')
        return x

    def clearButton(self, x,y):
        if(84 < x < 235) and (705 < y < 744):
            # print(f'this is x: {x}')
            # print(f' this is y: {y}')
            return True
        else:
            return False
    def menuButton(self, x, y):
        if (495 < x < 645) and (705 < y < 744):
            # print(f'x: {x}')
            # print(f'y: {y}')
            return True
        else:
            return False

#Game Running
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
                #if restart / startover / clear button is clicked
                pentago.clear_board("reset")
                board.draw_board(pentago.board, pentago.turn)
                board.draw_arrows(BLACK)
                pygame.display.update()

            elif pentago.board_full() and moveComplete:
                #if game ends in draw with board full
                pentago.state = 3

            elif event.type == pygame.MOUSEBUTTONDOWN and board.menuButton(event.pos[0], event.pos[1]):
                #if menu button clicked
                pentago.clear_board("menu")
                board.game_menu()
                pygame.display.update()


            elif pentago.state == -1:
                #start menu
                board.game_menu()
                pygame.display.update()

                pressed = -1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = board.gamemenuButton(event.pos[0], event.pos[1])

                if pressed == 0:
                    pentago.state = 1 # one player human first
                    pentago.humanfirst = True
                elif pressed == 1:
                    pentago.state = 0 # one player ai first
                    pentago.humanfirst = False
                elif pressed == 2:
                    pentago.state = 0 #two player
                    pentago.twoplayer = True
                else:
                    pentago.state = -1
            elif pentago.state == 2:
#               game won by one player
                if pentago.player1:
                    label = board.font_gameover.render(f"Game Over:  Player 1 Won!", 1, RED, BLACK)
                    board.screen.blit(label, (gameOver_dimension_x,gameOver_dimension_y))
                    pygame.display.update()
                if pentago.player2:
                    label = board.font_gameover.render(f"Game Over:  Player 2 Won!", 1, RED, BLACK)
                    board.screen.blit(label, (gameOver_dimension_x,gameOver_dimension_y))
                    pygame.display.update()
                pentago.state = 2
            elif pentago.state == 3:
#               game draw
                if pentago.draw:
                    label = board.font_gameover.render(f"       Game Over: Draw!    ", 1, RED, BLACK)
                    board.screen.blit(label, (gameOver_dimension_x,gameOver_dimension_y))
                    pygame.display.update()
                pentago.state = 3

            else:
                board.draw_board(pentago.board, pentago.turn)
                pygame.display.update()
                if pentago.turn == 1:
                    if pentago.state == 0:
                        #drop piece
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            moveComplete = False

                            x = event.pos[0]
                            y = event.pos[1]

                            col = board.whichRowCol(x)
                            row = board.whichRowCol(y)
                            if col == 0 or row == 0:
                                continue
                            else:
                                if pentago.turn == 0:
                                    pentago.drop_piece(row, col)
                                else:
                                    pentago.drop_piece(row, col)

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

                                pentago.turn += 1
                                pentago.turn = pentago.turn % 2

                                if pentago.state == 0 or pentago.state == 1:
                                    pentago.state += 1
                                    pentago.state = pentago.state % 2
                            board.draw_arrows(BLACK)
                            board.draw_board(pentago.board, pentago.turn)
                            pygame.display.update()
################################################################################
                elif pentago.turn == 0 and pentago.twoplayer:
                    if pentago.state == 0:
                        #drop piece
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            moveComplete = False

                            x = event.pos[0]
                            y = event.pos[1]

                            col = board.whichRowCol(x)
                            row = board.whichRowCol(y)
                            if col == 0 or row == 0:
                                continue
                            else:
                                if pentago.turn == 0:
                                    pentago.drop_piece(row, col)
                                else:
                                    pentago.drop_piece(row, col)

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

                                pentago.turn += 1
                                pentago.turn = pentago.turn % 2

                                if pentago.state == 0 or pentago.state == 1:
                                    pentago.state += 1
                                    pentago.state = pentago.state % 2
                            board.draw_arrows(BLACK)
                            board.draw_board(pentago.board, pentago.turn)
                            pygame.display.update()
################################################################################
                elif pentago.turn == 0 and not pentago.twoplayer:
                    if pentago.state == 0:
                        #drop piece
                        #If this is the AI's turn, then don't wait for a click event. instead,
                        #make sure the AI takes its turn.

                        #Take the scpre based on the current rotation
                        AI.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation)
                        AI_Defense.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation)
                        moveComplete = False
                        high_score_defense = 0
                        high_score_offense = 0
                        node_for_highest_score_defense,high_score_defense = AI_Defense.look_at_score_monomial()
                        node_for_highest_score_offense,high_score_offense = AI.look_at_score_monomial()


                        # print("This is the high_score for defense:"+ str(high_score_defense))
                        # print ("This is the high_score for offense" + str(high_score_offense))
                        if high_score_offense >= high_score_defense:
                            node_for_highest_score = node_for_highest_score_offense
                        else:
                            node_for_highest_score = node_for_highest_score_defense
                        # print("This is the node: "+str(node_for_highest_score))
                        #get scores based on offense and defense
##                        highest_score = -1
##                        highest_score_offensive = -1
##                        highest_score_defensive = -1
##                        go_defense = False
##                        go_offense = False
##                        node_list_offense = AI.look_at_scores()
##                        node_list_defense = AI_Defense.look_at_scores()
##                        node_list_offense_randomness = node_list_offense.copy()
##                        node_list_defense_randomness = node_list_defense.copy()
##                        node_list_offense_2 = []
##                        node_list_defense_2 = []
##                        node_list_select_place = []
                        #compare all scores for offense and defense
                        #get the highest one to put piece in there
##                        for i in range(36):
##                            if node_list_offense[i] >= highest_score_offensive:
##                                highest_score_offensive = node_list_offense[i]
##                            if node_list_defense[i] >= highest_score_defensive:
##                                highest_score_defensive = node_list_defense[i]
##                            if node_list_offense[i] >= highest_score:
##                                highest_score = node_list_offense[i]
##                                #node_for_highest_score = i
##                            if node_list_defense[i] >= highest_score:
##                                highest_score = node_list_defense[i]

                                #node_for_highest_score = i
                        #print ("Highest score is: " + str(highest_score))
##                        for i in range(36):
##                            #if node_list_offense[i] >= highest_score_defensive:
##                                #node_list_offense_2.append(i)
##                                #print ("This is offense " + str(i) + ": " + str(node_list_offense[i]))
##                            #if node_list_defense[i] >= highest_score:
##                                #node_list_defense_2.append(i)
##                                #go_defense = True
##                                #print ("This is defense " + str(i) + ": " + str(node_list_defense[i]))
##
##                            if node_list_offense[i] >= highest_score:
##                                print ("This is offense " + str(i) + ": " + str(node_list_offense[i]))
##                                go_offense = True
##                                node_list_offense_2.append(i)
##                            if node_list_defense[i] >= highest_score:
##                                print ("This is defense " + str(i) + ": " + str(node_list_defense[i]))
##                                go_defense = True
##                                node_list_defense_2.append(i)

                            #if go_offense == True and highest_score >= 2000:
                                #go_defense = False

                        #for i in range(len(node_list_offense_2)):
                            #node_list_select_place.append(node_list_offense_2[i])
                        #for i in range(len(node_list_defense_2)):
                            #node_list_select_place.append(node_list_defense_2[i])

##                        if go_offense == True:
##                            node_for_highest_score = random.choice(node_list_offense_2)
##                            go_offense = False
##                        else:
##                            node_for_highest_score = random.choice(node_list_defense_2)
##
                        #if go_defense == True:
                            #node_for_highest_score = random.choice(node_list_defense_2)
                            #go_defense = False
                        #else:
                            #node_for_highest_score = random.choice(node_list_offense_2)
                        #node_for_highest_score = random.choice(node_list_select_place)

                        # refactored the if statements
                        # figuring out quad for searching row, col in board hash

                        if (node_for_highest_score in BoardHash.quad_0_variables):
                            quad_for_highest_score = 0
                        if (node_for_highest_score in BoardHash.quad_1_variables):
                            quad_for_highest_score = 1
                        if (node_for_highest_score in BoardHash.quad_2_variables):
                            quad_for_highest_score = 2
                        if (node_for_highest_score in BoardHash.quad_3_variables):
                            quad_for_highest_score = 3

                        # value of specific quad rotation.  quad_0_rotation, quad_1_rotation etc
                        # quad changes depending on which quad is highest score
                        quad_rotation = globals()[('quad_') + str(quad_for_highest_score) + ('_rotation')]

                        # print(f'quad for highest score: {quad_for_highest_score}')
                        # print(f'node for highest score: {node_for_highest_score}')
                        # print(f'quad rotation: {quad_rotation}')

                        row = BoardHash.board_hash[quad_for_highest_score][node_for_highest_score][quad_rotation][0]
                        col = BoardHash.board_hash[quad_for_highest_score][node_for_highest_score][quad_rotation][1]
                        # end of refactoring if statements



                        # print("row:" + str(row) + "| col:" + str(col))
                        pentago.drop_piece(row, col)

                        # # trigger mouse event so win message will display in case AI wins
                        pygame.event.post(pygame.event.Event(pygame.MOUSEMOTION,
                                                             {"pos": pygame.mouse.get_pos(), "rel": None,
                                                              "buttons": None}))
                        # print("AI piece dropped")

                        board.draw_board(pentago.board, pentago.turn)
                        pygame.display.update()

                        node_for_highest_score = 0


                    if pentago.state == 1:
                        #rotate quadrant
                        quad_0_rotation_right = quad_0_rotation +1
                        quad_1_rotation_right = quad_1_rotation +1
                        quad_2_rotation_right = quad_2_rotation +1
                        quad_3_rotation_right = quad_3_rotation +1
                        quad_0_rotation_left = quad_0_rotation -1
                        quad_1_rotation_left = quad_1_rotation -1
                        quad_2_rotation_left = quad_2_rotation -1
                        quad_3_rotation_left = quad_3_rotation -1
                        high_score = 0
                        right_0 = 0
                        left_0 = 0
                        right_1 = 0
                        left_1 = 0
                        right_2 = 0
                        left_2 = 0
                        right_3 = 0
                        left_3 = 0
                        right_0_defense = 0
                        left_0_defense = 0
                        right_1_defense = 0
                        left_1_defense = 0
                        right_2_defense = 0
                        left_2_defense = 0
                        right_3_defense = 0
                        left_3_defense = 0
                        go_defense_rotation = False



                        right_0 = AI.score_taking_rotations(quad_0_rotation_right, quad_1_rotation, quad_2_rotation, quad_3_rotation)
                        #print("right_0")
                        left_0 = AI.score_taking_rotations(quad_0_rotation_left, quad_1_rotation, quad_2_rotation, quad_3_rotation)
                        #print("left_0")
                        right_1 = AI.score_taking_rotations(quad_0_rotation, quad_1_rotation_right, quad_2_rotation, quad_3_rotation)
                        #print("right_1")
                        left_1 = AI.score_taking_rotations(quad_0_rotation, quad_1_rotation_left, quad_2_rotation, quad_3_rotation)
                        #print("left_1")
                        right_2 = AI.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation_right, quad_3_rotation)
                        #print("right_2")
                        left_2 = AI.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation_left, quad_3_rotation)
                        #print("left_2")
                        right_3 = AI.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation_right)
                        #print("right_3")
                        left_3 = AI.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation_left)

############################################################################################################################################
                        right_0_defense = AI_Defense.score_taking_rotations(quad_0_rotation_right, quad_1_rotation, quad_2_rotation, quad_3_rotation)
                        #print("right_0")
                        left_0_defense = AI_Defense.score_taking_rotations(quad_0_rotation_left, quad_1_rotation, quad_2_rotation, quad_3_rotation)
                        #print("left_0")
                        right_1_defense = AI_Defense.score_taking_rotations(quad_0_rotation, quad_1_rotation_right, quad_2_rotation, quad_3_rotation)
                        #print("right_1")
                        left_1_defense = AI_Defense.score_taking_rotations(quad_0_rotation, quad_1_rotation_left, quad_2_rotation, quad_3_rotation)
                        #print("left_1")
                        right_2_defense = AI_Defense.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation_right, quad_3_rotation)
                        #print("right_2")
                        left_2_defense = AI_Defense.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation_left, quad_3_rotation)
                        #print("left_2")
                        right_3_defense = AI_Defense.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation_right)
                        #print("right_3")
                        left_3_defense = AI_Defense.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation_left)





                        #print("left_3")
                        #print ("quad 0: " + str(left_0) + "," + str(right_0))
                        #print ("quad 1: " + str(left_1) + "," + str(right_1))
                        #print ("quad 2: " + str(left_2) + "," + str(right_2))
                        #print ("quad 3: " + str(left_3) + "," + str(right_3))

##                        print ("right_0: " + str(right_0))
##                        print ("left_0: " + str(left_0))
##                        print ("right_1: " + str(right_1))
##                        print ("left_1: " + str(left_1))
##                        print ("right_2: " + str(right_2))
##                        print ("left_2: " + str(left_2))
##                        print ("right_3: " + str(right_3))
##                        print ("left_3: " + str(left_3))


                        if right_0 > high_score:
                            high_score = right_0
                            quad = 0
                            rotation = 0
                            #print("This is an offensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            #print("here")
                        if left_0 > high_score:
                            high_score = left_0
                            quad = 0
                            rotation = 1
                            #print("This is an offensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            #print("here")
                        if right_1 > high_score:
                            high_score = right_1
                            quad = 1
                            rotation = 0
                            #print("This is an offensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                        if left_1 > high_score:
                            high_score = left_1
                            quad = 1
                            rotation = 1
                            #print("This is an offensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                        if right_2 > high_score:
                            high_score = right_2
                            quad = 2
                            rotation = 0
                            #print("This is an offensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                        if left_2 > high_score:
                            high_score = left_2
                            quad = 2
                            rotation = 1
                            #print("This is an offensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                        if right_3 > high_score:
                            high_score = right_3
                            quad = 3
                            rotation = 0
                            #print("This is an offensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                        if left_3 > high_score:
                            high_score = left_3
                            quad = 3
                            rotation = 1
                            #print("This is an offensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))



##                        print ("right_0_defense: " + str(right_0_defense))
##                        print ("left_0_defense: " + str(left_0_defense))
##                        print ("right_1_defense: " + str(right_1_defense))
##                        print ("left_1_defense: " + str(left_1_defense))
##                        print ("right_2_defense: " + str(right_2_defense))
##                        print ("left_2_defense: " + str(left_2_defense))
##                        print ("right_3_defense: " + str(right_3_defense))
##                        print ("left_3_defense: " + str(left_3_defense))
##
                        if right_0_defense >= high_score:
                            high_score = right_0_defense
                            go_defense_rotation = True
                        if left_0_defense >= high_score:
                            high_score = left_0_defense
                            go_defense_rotation = True
                        if right_1_defense >= high_score:
                            high_score = right_1_defense
                            go_defense_rotation = True
                        if left_1_defense >= high_score:
                            high_score = left_1_defense
                            go_defense_rotation = True
                        if right_2_defense >= high_score:
                            high_score = right_2_defense
                            go_defense_rotation = True
                        if left_2_defense >= high_score:
                            high_score = left_2_defense
                            go_defense_rotation = True
                        if right_3_defense >= high_score:
                            high_score = right_3_defense
                            go_defense_rotation = True
                        if left_3_defense >= high_score:
                            high_score = left_3_defense
                            go_defense_rotation = True

                        if go_defense_rotation == True:
                            go_defense_rotation = False
                            high_score = high_score +1
                            if right_0_defense < high_score:
                                high_score = right_0_defense
                                quad = 0
                                rotation = 0
                                #print("This is an defensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            if left_0_defense < high_score:
                                high_score = left_0_defense
                                quad = 0
                                rotation = 1
                                #print("This is an defensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            if right_1_defense < high_score:
                                high_score = right_1_defense
                                quad = 1
                                rotation = 0
                                #print("This is an defensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            if left_1_defense < high_score:
                                high_score = left_1_defense
                                quad = 1
                                rotation = 1
                                #print("This is an defensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            if right_2_defense < high_score:
                                high_score = right_2_defense
                                quad = 2
                                rotation = 0
                                #print("This is an defensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            if left_2_defense < high_score:
                                high_score = left_2_defense
                                quad = 2
                                rotation = 1
                                #print("This is an defensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            if right_3_defense < high_score:
                                high_score = right_3_defense
                                quad = 3
                                rotation = 0
                                #print("This is an defensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))
                            if left_3_defense < high_score:
                                high_score = left_3_defense
                                quad = 3
                                rotation = 1
                                #print("This is an defensive rotation on quad: " + str(quad)+ " with rotation, " + str(rotation))




                        #print("highscore: " + str(high_score))

                        pentago.rotate_quad(quad, rotation)
                        board.draw_board(pentago.board, pentago.turn)

                        pygame.display.update()
                        moveComplete = True
                        pentago.turn += 1
                        # print(pentago.turn)
                        if pentago.state == 0 or pentago.state == 1:
                            pentago.state += 1
                            pentago.state = pentago.state % 2
                        board.draw_arrows(BLACK)
                        board.draw_board(pentago.board, pentago.turn)
                        pygame.display.update()

running()
