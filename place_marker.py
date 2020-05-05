from display_board import display_board

def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)
    print('hello')
