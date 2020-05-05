from choose_first import choose_first
from display_board import display_board
from full_board import full_board_check
from place_marker import place_marker
from player_choice import player_choice
from player_input import player_input
from replay import replay
from space_check import space_check
from win_check import win_check

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here, choose who's first, choose marker
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    
    print(turn + ' will go first. ')
    
    play_game = input('Ready to play? \'y\' or \'n\' ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == "Player 1":
            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board,turn)
            # place the marker on that postion and display the board
            place_marker(the_board, player1_marker, position)
            #check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 HAS WON')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('GAME DRAW')
                    game_on = False
                else:
                    turn = 'Player 2'      
        else:
            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board,turn)
            # place the marker on that postion and display the board
            place_marker(the_board, player2_marker, position)
            #check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 HAS WON')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('GAME DRAW.')
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay():
        break