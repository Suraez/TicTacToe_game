def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Enter Player 1 input: 'X' or 'O' ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
