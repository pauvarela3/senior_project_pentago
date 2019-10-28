import numpy as np
import pygame 
import sys
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

radius = int(indsqu/2 - 5)

squares = 4
rows = 3 
columns = 3 

turn = 0
state = -1

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
        return -1
    
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
    game_over = False

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
    left = 1
    right = 0
    game_over = False
    
    if rotation == left:
        board[quad] = list(zip(*reversed(board[quad])))
        board[quad] = list(zip(*reversed(board[quad])))
        board[quad] = list(zip(*reversed(board[quad])))
    elif rotation == right:
        board[quad] = list(zip(*reversed(board[quad])))
        
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
            game_menu(screen, event)
        elif pressed == 0:
            return pressed
        elif pressed == 1:
            return pressed
        else:
            game_menu(screen, event)
def game_over_sign(x,y):
    pressed = 1
    return pressed
    pass

            
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
        default_font = pygame.font.get_default_font()
        font_renderer = pygame.font.Font(default_font, 32)
        font_gameover = pygame.font.Font(default_font, 45)
        if event.type == MOUSEBUTTONDOWN and in_range(event.pos[0], event.pos[1]):
            board, turn, game_over, state = clear_board()
            draw_board(screen, board)
            pygame.display.update()
        if state == -1:
            pressed = game_menu(screen, event)
            if pressed == 0: #one player
                state = 0
            if pressed == 1: #two player
                state = 0
                
        else: 
            if not game_over:
                label = font_gameover.render(f"Game Over: Player {turn + 1} Won!", 1, BLACK, BLACK)
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
                            
                    
                    if  state_pass == 1:
                        state += 1
                    else:
                        state = 0
                    if game_over:
                        label = font_gameover.render(f"Game Over: Player {turn + 1} Won!", 1, RED, BLACK)
                        screen.blit(label, (65,340))
                        pygame.display.update()
                        print("here")
                        if event.type == MOUSEBUTTONDOWN:
                            pressed = game_over_sign(event.pos[0], event.pos[1])
    
                            if pressed == 0:
                                board, turn, game_over, state = clear_board()
                                draw_board(screen, board)
                                pygame.display.update()
    
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0]
                    y = event.pos[1]
                    
                    
                    quad = check_quad(x, y)
                    quad_done = True
                    
                if event.type == pygame.KEYDOWN and quad_done == True:
                    if event.key == pygame.K_LEFT:
                        rotation = 1
                    if event.key == pygame.K_RIGHT:
                        rotation = 0
                    
                            
                    board, game_over = rotate_quad(board, quad, rotation, piece)
                    
                    
                    turn = new  
                    state += 1
                    state = state % 2
                    quad_done = False
                    
                    if game_over:
                        checked = True
                        while not checked:
                            label = font_gameover.render(f"Game Over: Player {turn + 1} Won!", 1, RED, BLACK)
                            screen.blit(label, (65,340))
                            pygame.display.update()
                            print("here")
                            
                        board, turn, game_over, state = clear_board()
                        draw_board(screen, board)
                        pygame.display.update()
            
                    pygame.display.update()
