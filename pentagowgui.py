import numpy as np
import pygame 
import sys
import AI
from pygame.constants import MOUSEBUTTONDOWN

pygame.init()

SQUARESIZE = 90 * 3
squarescreen = 90 * 8
COL = 6
ROW = 6
state_pass = 0
indsqu = 90

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
DARK_RED = (169,0,0)
WHITE = (255,255,255)
GRAY = (131,139,139)
GREEN = (0,255,0)
YELLOW = (0, 127,127)

radius = int(indsqu/2 - 5)

squares = 4
rows = 3 
columns = 3 
quad_0_rotation = 0
quad_1_rotation = 0
quad_2_rotation = 0
quad_3_rotation = 0
turn = 0
state = -1

rotate_right = False
rotate_left = False

game_over = False
quad_done = False

board = np.zeros((squares, rows, columns))

size = (squarescreen, squarescreen + 65)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pentago")


running = True


def check_range(value):
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
    else: x = 0
    
    return x

def check_quad(x, y):
    col = x
    row = y
    
    if (row >65 and row <335) and (col > 65 and col < 335):
        return 0
    elif (row >65 and row <335) and (col > 380 and col <650):
        return 1
    elif (row > 380 and row <650) and (col >65 and col <335):
        return 2
    elif (row > 380 and row <650) and (col > 380 and col <650):
        return 3
    else:
        return 5
    
def in_range(x,y):
    if(x > 65 and x <223) and (y > 713 and y < 744):
        return True  
    else:
        return False 
    
def check_pressed(x,y):
    if( 219 < x and x < 501) and (259 < y and y < 359):
        return 0
    
    elif (219 < x and x < 501) and (399 < y and y < 501):
        return 1
    else:
        return -1


def draw_board(screen, board):
    
    pygame.draw.rect(screen, BLACK, (65, 65, (SQUARESIZE * 2) + 45, (SQUARESIZE * 2) + 45))
    
    pygame.draw.rect(screen, RED, (65,65,SQUARESIZE, SQUARESIZE), 2)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen,RED, ((c*indsqu)+65, (r*indsqu)+65, indsqu, indsqu))
            
            if board[0][r][c] == 0:
                pygame.draw.circle(screen,DARK_RED, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+65), radius)
            if board[0][r][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+65), radius)
            if board[0][r][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+65), radius)


    pygame.draw.rect(screen, RED, (SQUARESIZE + 110, 65, SQUARESIZE, SQUARESIZE), 2)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen,RED, ((c*indsqu)+110 + SQUARESIZE, (r*indsqu)+65, indsqu, indsqu))
            
            if board[1][r][c] == 0:
                pygame.draw.circle(screen,DARK_RED, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+65), radius)
            if board[1][r][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+65), radius)
            if board[1][r][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+65), radius)

    pygame.draw.rect(screen, RED, (65, 110 + SQUARESIZE, SQUARESIZE, SQUARESIZE), 2)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen,RED, ((c*indsqu)+65, (r*indsqu)+110 + SQUARESIZE, indsqu, indsqu))
            
            if board[2][r][c] == 0:
                pygame.draw.circle(screen,DARK_RED, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+380), radius)
            if board[2][r][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+380), radius)
            if board[2][r][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*indsqu+(indsqu/2))+65, int(r*indsqu+(indsqu/2))+380), radius)

    pygame.draw.rect(screen, RED, (SQUARESIZE + 110, 110 + SQUARESIZE, SQUARESIZE, SQUARESIZE), 2)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen,RED, ((c*indsqu)+110 +SQUARESIZE, (r*indsqu)+110 + SQUARESIZE, indsqu, indsqu))
            
            if board[3][r][c] == 0:
                pygame.draw.circle(screen,DARK_RED, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+380), radius)
            if board[3][r][c] == 1:
                pygame.draw.circle(screen,WHITE, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+380), radius)
            if board[3][r][c] == 2:
                pygame.draw.circle(screen,BLACK, (int(c*indsqu+(indsqu/2))+380, int(r*indsqu+(indsqu/2))+380), radius)

def drop_piece(row, col, board, turn, piece):
    global quad_0_rotation
    global quad_1_rotation
    global quad_2_rotation
    global quad_3_rotation
    game_over = False
    variable_number = 0
    if row > 3 and col > 3:
        quad = 3
        row = row - 4
        col = col - 4
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
    AI.score_taking(variable_number,turn)
    if turn ==0:
        piece = 1
    else:
        piece = 2
        

    
    if not valid_move(row, col, quad):
        print("Space is already occupied, select another place")
        return turn, game_over
    else:
        turn += 1
        turn = turn % 2
        board[quad][row][col] = piece
        
        if winning_move(board, piece):
            game_over = True
            print(f'Congrats Player {piece}, you have won the game!')

        return turn, game_over


def valid_move(row, col, quad):
    global state_pass
    if board[quad][row][col] == 0:
        state_pass = 1
        return True
    else:
        state_pass = 0
        return False

def rotate_quad(board, quad, rotation, piece):
    global quad_0_rotation
    global quad_1_rotation
    global quad_2_rotation
    global quad_3_rotation
    left = 1
    right = 0
    game_over = False


    #Here the AI is going to check both left and right rotation scores
    #It should decide which rotation should it do by looking at every
    #individual monomial and depending on which one has the highest score,
    #it will rotate that way.
    
    if rotation == left:
        board[quad] = list(zip(*reversed(board[quad])))
        board[quad] = list(zip(*reversed(board[quad])))
        board[quad] = list(zip(*reversed(board[quad])))
        if quad == 0:
            quad_0_rotation = quad_0_rotation - 1
        elif quad == 1:
            quad_1_rotation = quad_1_rotation - 1
        elif quad == 2:
            quad_2_rotation = quad_2_rotation - 1
        else:
            quad_3_rotation = quad_3_rotation - 1
    elif rotation == right:
        board[quad] = list(zip(*reversed(board[quad])))
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
    print (quad_0_rotation)
    print (quad_1_rotation)
    print (quad_2_rotation)
    print (quad_3_rotation)
    print ("These were the rotations")
    AI.score_taking_rotations(quad_0_rotation, quad_1_rotation, quad_2_rotation, quad_3_rotation)    
    
    if winning_move(board, piece):
        game_over = True
        print(f'Congrats Player {piece}, you have won the game!')
        
    return board, game_over

def winning_move(board, piece):
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

def clear_board():
    board = np.zeros((squares, rows, columns))
    turn = 0
    game_over = False
    state = 0

    return board, turn, game_over, state

def checkrange(x,y):
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


def draw_arrows(screen, color):
    
    x = 15
    y = 70
    pygame.draw.polygon(screen, color, ((16+x,10+y),(16+x,50+y),(8+x,50+y),(23+x,75+y),(38+x,50+y),(30+x,50+y),(30+x,10+y)))
     
    x = 655
    y = 70 
    pygame.draw.polygon(screen, color, ((16+x,10+y),(16+x,50+y),(8+x,50+y),(23+x,75+y),(38+x,50+y),(30+x,50+y),(30+x,10+y)))
    
    x = 70
    y = 15
    pygame.draw.polygon(screen, color, ((10+x,16+y),(50+x,16+y),(50+x,8+y),(75+x,23+y),(50+x,38+y),(50+x,30+y),(10+x,30+y)))
                        
    x = 70
    y = 655
    pygame.draw.polygon(screen, color, ((10+x,16+y),(50+x,16+y),(50+x,8+y),(75+x,23+y),(50+x,38+y),(50+x,30+y),(10+x,30+y)))

    x = 655
    y = 570
    pygame.draw.polygon(screen, color, ((16+x,75+y),(16+x,35+y),(8+x,35+y),(23+x,10+y),(38+x, 35+y),(30+x,35+y),(30+x,75+y)))

    x = 15
    y = 570
    pygame.draw.polygon(screen, color, ((16+x,75+y),(16+x,35+y),(8+x,35+y),(23+x,10+y),(38+x,35+y),(30+x,35+y),(30+x,75+y)))


    x = 570
    y = 15
    pygame.draw.polygon(screen, color, ((10+x,23+y),(35+x,8+y),(35+x,16+y),(75+x,16+y),(75+x,30+y),(35+x,30+y),(35+x,38+y)))
    
    x = 570
    y = 655
    pygame.draw.polygon(screen, color, ((10+x,23+y),(35+x,8+y),(35+x,16+y),(75+x,16+y),(75+x,30+y),(35+x,30+y),(35+x,38+y)))



def game_menu(screen, event):
    default_font = pygame.font.get_default_font()
    font_renderer = pygame.font.Font(default_font, 80)
    label = font_renderer.render("PENTAGO", 1, RED)
    screen.blit(label, (165,120))
    coord = (135, 220, 450, 320)
    pygame.draw.rect(screen, BLUE, coord)
    button1 = (220, 260, 280, 100)
    pygame.draw.rect(screen, BLACK, button1)
    button3 = (220, 400, 280, 100)
    pygame.draw.rect(screen, BLACK, button3)
    
    font_label = pygame.font.Font(default_font, 32)
    font_tiny = pygame.font.Font(default_font, 32)
    label1 = font_label.render("Start Game:", 1, RED)
    label12 = font_tiny.render("One Player", 1, RED)
    label2 = font_label.render("Start Game:", 1, RED)
    label22 = font_tiny.render("Two Player", 1, RED)
    
    screen.blit(label1, (265, 280))
    screen.blit(label12, (270, 310))
    screen.blit(label2, (265, 420))
    screen.blit(label22, (270, 450))
            
    pygame.display.update()
    
    if event.type == MOUSEBUTTONDOWN:
        pressed = check_pressed(event.pos[0], event.pos[1])
        if pressed == -1:
            pass
        elif pressed == 0:
            return pressed
        elif pressed == 1:
            return pressed
        else:
            pass
def game_over_sign(x,y):
    pressed = 1
    return pressed

def board_full(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            for k in range(len(board[0][0])):
                if board[i][j][k] == 0:
                    game_over = False
                    return False, game_over
                
    game_over = True
    return True, game_over


def pushMove(chipMoves, rotationMoves, piece, rotation):
    chipMoves.append(piece)
    rotationMoves.append(rotation)

def popMove(chipMoves, rotationMoves, state):
    if state == 0:
        #remove just the piece that was placed
        return chipMoves.pop()
    elif state == 1:
        #remove the piece AND the rotation
        return chipMoves.pop(), rotationMoves.pop()
    else:
        pass
           
            
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
        default_font = pygame.font.get_default_font()
        font_renderer = pygame.font.Font(default_font, 32)
        font_gameover = pygame.font.Font(default_font, 45)
        boardfull, game_over = board_full(board)
        if boardfull == True:
            label = font_gameover.render(f"Game Over: Draw", 1, RED, BLACK)
            screen.blit(label, (65,340))
            pygame.display.update()
            state = -2
        elif event.type == MOUSEBUTTONDOWN and in_range(event.pos[0], event.pos[1]):
            board, turn, game_over, state = clear_board()
            draw_board(screen, board)
            pygame.display.update()
        elif state == -2:
            pass
        elif state == -1:
            pressed = game_menu(screen, event)
            if pressed == 0: #one player
                state = 0
            if pressed == 1: #two player
                state = 0
                
        else: 
            if not game_over:
                label = font_gameover.render(f"Game Over:  Player {turn + 1} Won!", 1, BLACK, BLACK)
                screen.blit(label, (65,340))
                draw_board(screen, board)
                label = font_renderer.render(f"Turn: Player {turn + 1}", 1, WHITE, BLACK)
                screen.blit(label, (245,670))
                label = font_renderer.render("  Start Over  ", 1, WHITE, GRAY)
                screen.blit(label, (65, 710))

            
            pygame.display.update()
            if state == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                   
                    x = event.pos[0]
                    y = event.pos[1]
                        
                    col = check_range(x)
                    row = check_range(y)
                    if col == 0 or row == 0:
                        continue
                    else:
                        if turn == 0:
                            piece = 1
                            new, game_over = drop_piece(row, col, board, turn, piece)
                        else:
                            piece = 2
                            new, game_over = drop_piece(row, col, board, turn, piece)
                    
                    
                    draw_board(screen, board)
                    pygame.display.update()        
                    
                    if  state_pass == 1:
                        state += 1
                    else:
                        state = 0
                    if game_over:
                        draw_board(screen, board)
                        label = font_gameover.render(f"Game Over:  Player {turn + 1} Won!", 1, RED, BLACK)
                        screen.blit(label, (65,340))
                        pygame.display.update()
                        print("here")
                        state = -2
                        if event.type == MOUSEBUTTONDOWN:
                            pressed = game_over_sign(event.pos[0], event.pos[1])
    
                            if pressed == 0:
                                board, turn, game_over, state = clear_board()
                                draw_board(screen, board)
                                pygame.display.update()
    
            else:
                draw_arrows(screen, GRAY)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0]
                    y = event.pos[1]
                    
                    
#                     quad = check_quad(x, y)
#                     if quad == 5:
#                         quad_done = False
#                     else:
#                         quad_done = True
#                     
#                     
#                 if event.type == pygame.KEYDOWN and quad_done == True:
#                     if event.key == pygame.K_LEFT:
#                         rotation = 1
#                     if event.key == pygame.K_RIGHT:
#                         rotation = 0
                    
                    #print(x, y)
                    quad, rotation = checkrange(x, y)
                    #print(quad, rotation)
                    
                                                
                    if quad == 5 and rotation == 5:
                        pass
                    else:
                        
                        board, game_over = rotate_quad(board, quad, rotation, piece)
                        draw_arrows(screen, BLACK)
                        pygame.display.update()

                        turn = new  
                        state += 1
                        state = state % 2
                        quad_done = False
                        
                        
                        if game_over:
                            draw_board(screen, board)
                            label = font_gameover.render(f"Game Over:  Player {turn + 1} Won!", 1, RED, BLACK)
                            screen.blit(label, (65,340))
                            pygame.display.update()
                            print("here")
                            state = -2
                            if event.type == MOUSEBUTTONDOWN:
                                pressed = game_over_sign(event.pos[0], event.pos[1])
        
                                if pressed == 0:
                                    board, turn, game_over, state = clear_board()
                                    draw_board(screen, board)
                                    pygame.display.update()
                                    
            
                    pygame.display.update()
