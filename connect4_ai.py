from connect4_functions import minimax_algo,pick_best_move, init_game, winning_move, print_board, drop_piece, is_valid_location, get_next_open_row,NUM_COL,NUM_ROW , PLAYER, AI , PLAYR_PCE, AI_PCE
from connect4_gui import init_gui, draw_board, pygame, SQUARESIZE, RADIUS, RED, YELLOW, BLACK, width, height
import math, random, sys




def main():
    board, game_over, turn = init_game()
    screen,font = init_gui()
    draw_board(board, screen)
    pygame.display.update()

    turn = random.randint(PLAYER,AI)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                
            pygame.display.update()

                    


            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
            #Player 1
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))
                    if is_valid_location(board,col):
                        row = get_next_open_row(board,col)
                        drop_piece(board,row,col,PLAYR_PCE)

                        if winning_move(board, PLAYR_PCE):
                            label = font.render("Player 1 Wins!", 1, RED)
                            screen.blit(label,(40,10))
                            game_over = True

                        turn+=1
                        turn = turn%2

                        print_board(board)    
                        draw_board(board,screen)
                            

        if turn == AI and not game_over:
            
            col, minimax_score= minimax_algo(board,4,-math.inf,math.inf,True)


            if is_valid_location(board,col):
                pygame.time.wait(500)
                row = get_next_open_row(board,col)
                drop_piece(board,row,col,AI_PCE)

                if winning_move(board,AI_PCE):
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
