from space_check import space_check
def player_choice(board, turn):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input( turn + ': choose the position (1-9) '))
        
    return position

    