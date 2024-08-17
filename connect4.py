from connect4_functions import init_game, winning_move, print_board, drop_piece, is_valid_location, get_next_open_row
from connect4_gui import init_gui, draw_board, pygame, SQUARESIZE, RADIUS, RED, YELLOW, BLACK, width, height
import sys
import math


def main():
    board, game_over, turn = init_game()
    screen,font = init_gui()
    draw_board(board, screen)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

                    


            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
            #Player 1
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))
                    if is_valid_location(board,col):
                        row = get_next_open_row(board,col)
                        drop_piece(board,row,col,1)
                        if winning_move(board,1):
                            label = font.render("Player 1 Wins!", 1, RED)
                            screen.blit(label,(40,10))
                            game_over = True
                            

                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))
                    if is_valid_location(board,col):
                        row = get_next_open_row(board,col)
                        drop_piece(board,row,col,2)

                        if winning_move(board,2):
                            label = font.render("Player 2 Wins!", 1, YELLOW)
                            screen.blit(label,(40,10))
                            game_over = True
                print_board(board)    
                draw_board(board,screen)        
                turn+=1
                turn = turn%2
                if game_over == True:
                    pygame.time.wait(3000)

           
if __name__ == "__main__":
    main()
