def valid_moves(piece, current_board):
    moves = []
    oob = []
    board_state = [[piece[0], piece[1]] for piece in current_board]
    valid = [[a, b] for a in range(8) for b in range(8) if [a, b] != [piece[0], piece[1]]]
    if 'king' in piece[2]:
        moves += [[a, b] for a in range(piece[0] - 1, piece[0] + 2) for b in range(piece[1] - 1, piece[1] + 2)]
    elif 'queen' in piece[2]:
        moves += valid_moves(piece[0:2] + ['rook'], current_board) + valid_moves(piece[0:2] + ['bishop'], current_board)
    elif 'rook' in piece[2]:
        moves += [[piece[0], a] for a in range(0, 8)] + [[b, piece[1]] for b in range(0, 8)]
    elif 'bishop' in piece[2]:
        moves += [[piece[0] + a, piece[1] - a] for a in range(-7, 8)] + \
                 [[piece[0] + a, piece[1] + a] for a in range(-7, 8)]
    elif 'knight' in piece[2]:
        moves += [[piece[0] + 1, piece[1] + 2], [piece[0] + 1, piece[1] - 2], [piece[0] - 1, piece[1] + 2],
                  [piece[0] - 1, piece[1] - 2], [piece[0] + 2, piece[1] + 1], [piece[0] + 2, piece[1] - 1],
                  [piece[0] - 2, piece[1] + 1], [piece[0] - 2, piece[1] - 1]]
    elif 'pawn' in piece[2]:
        if piece[2][0] == 'w':
            if piece[1] == 6:
                moves += [[piece[0], piece[1] - 1], [piece[0], piece[1] - 2]]
            else:
                moves += [[piece[0], piece[1] - 1]]
            moves += [move[0:2] for move in current_board if
                      (move[1] == piece[1] - 1 and abs(piece[0] - move[0]) == 1 and piece[2][0] != move[2][0])]
        elif piece[2][0] == 'b':
            if piece[1] == 1:
                moves += [[piece[0], piece[1] + 1], [piece[0], piece[1] + 2]]
            else:
                moves += [[piece[0], piece[1] + 1]]
            moves += [move[0:2] for move in current_board if
                      (move[1] == piece[1] + 1 and abs(piece[0] - move[0]) == 1 and piece[2][0] != move[2][0])]
    for move in moves:
        if move in board_state:
            if move[0] > piece[0]:
                if move[1] > piece[1]:
                    oob += [[a, b] for a in range(move[0] + 1, 8) for b in range(move[1], 8)]
                elif move[1] == piece[1]:
                    oob += [[a, piece[1]] for a in range(move[0] + 1, 8)]
                elif move[1] < piece[1]:
                    oob += [[a, b] for a in range(move[0], 8) for b in range(0, move[1])]
            elif move[0] == piece[0]:
                if move[1] > piece[1]:
                    oob += [[piece[0], b] for b in range(move[1] + 1, 8)]
                elif move[1] < piece[1]:
                    oob += [[piece[0], b] for b in range(0, move[1])]
            else:
                if move[1] > piece[1]:
                    oob += [[a, b] for a in range(0, move[0]) for b in range(move[1], 8)]
                elif move[1] == piece[1]:
                    oob += [[a, piece[1]] for a in range(0, move[0])]
                else:
                    oob += [[a, b] for a in range(0, move[0]) for b in range(0, move[1])]
    if 'pawn' not in piece[2]:
        oob += [move[0:2] for move in current_board if (move[2][0] == piece[2][0])]
    else:
        oob += [move[0:2] for move in current_board if move[0] == piece[0]]
    return [move for move in moves if (move in valid and not move in oob)]
