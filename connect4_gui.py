import pygame
import os 
from connect4_functions import NUM_COL,NUM_ROW , PLAYER, PLAYR_PCE, AI, AI_PCE

SQUARESIZE = 100
BLACK = (0,0,0)
PURPLE = (25,8,86)
RED = (255,0,0)
YELLOW = (255,255,0)
width = NUM_COL * SQUARESIZE
height = (NUM_ROW+1) * SQUARESIZE
size = (width,height)
RADIUS = int(SQUARESIZE/2 - 6)



def init_gui():
    pygame.init()
    screen = pygame.display.set_mode(size)
    font_size = 75
    font_name = "connect4_font.otf"
    font = pygame.font.Font(font_name,font_size)
    return screen,font

def draw_board(board, screen):
    for c in range(NUM_COL):
        for r in range(NUM_ROW):
            pygame.draw.rect(screen, PURPLE, (c*SQUARESIZE, height - (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(height - (r*SQUARESIZE+SQUARESIZE/2))), RADIUS)

    for c in range(NUM_COL):
        for r in range(NUM_ROW):
            if board[r][c] == PLAYR_PCE:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(height - (r*SQUARESIZE+SQUARESIZE/2))), RADIUS)
            elif board[r][c] == AI_PCE:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int(height - (r*SQUARESIZE+SQUARESIZE/2))), RADIUS)
    pygame.display.update()



