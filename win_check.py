def win_check(board, mark):
    return (all(board[i] == mark for i in range(7,10)) or
    all(board[i] == mark for i in range(4,7)) or
    all(board[i] == mark for i in range(1,4)) or
    all(board[i] == mark for i in range(1,8,3)) or
    all(board[i] == mark for i in range(2,9,3)) or
    all(board[i] == mark for i in range(3,10,3)) or
    all(board[i] == mark for i in range(1,10,4)) or
    all(board[i] == mark for i in range(3,8,2)))