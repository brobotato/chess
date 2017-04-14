def checker(square1, square2):
    board = []
    for x in range(0, 8, 2):
        for y in range(0, 8, 2):
            board.append([x, y, square1])
    for x in range(1, 9, 2):
        for y in range(1, 9, 2):
            board.append([x, y, square1])
    for x in range(0, 8, 2):
        for y in range(1, 9, 2):
            board.append([x, y, square2])
    for x in range(1, 9, 2):
        for y in range(0, 8, 2):
            board.append([x, y, square2])
    return board


def fill_pieces(color1, color2):
    piece_set = [
        [0, 0, color2 + 'rook'],
        [1, 0, color2 + 'knight'],
        [2, 0, color2 + 'bishop'],
        [3, 0, color2 + 'queen'],
        [4, 0, color2 + 'king'],
        [5, 0, color2 + 'bishop'],
        [6, 0, color2 + 'knight'],
        [7, 0, color2 + 'rook'],
        [0, 1, color2 + 'pawn'],
        [1, 1, color2 + 'pawn'],
        [2, 1, color2 + 'pawn'],
        [3, 1, color2 + 'pawn'],
        [4, 1, color2 + 'pawn'],
        [5, 1, color2 + 'pawn'],
        [6, 1, color2 + 'pawn'],
        [7, 1, color2 + 'pawn'],
        [0, 7, color1 + 'rook'],
        [1, 7, color1 + 'knight'],
        [2, 7, color1 + 'bishop'],
        [3, 7, color1 + 'queen'],
        [4, 7, color1 + 'king'],
        [5, 7, color1 + 'bishop'],
        [6, 7, color1 + 'knight'],
        [7, 7, color1 + 'rook'],
        [0, 6, color1 + 'pawn'],
        [1, 6, color1 + 'pawn'],
        [2, 6, color1 + 'pawn'],
        [3, 6, color1 + 'pawn'],
        [4, 6, color1 + 'pawn'],
        [5, 6, color1 + 'pawn'],
        [6, 6, color1 + 'pawn'],
        [7, 6, color1 + 'pawn'],
    ]
    return piece_set


def search_piece(coords,color,pieces):
    piece_set = [piece[0:2] for piece in pieces]
    if coords in piece_set:
        if pieces[piece_set.index(coords)][2][0] == color:
            return piece_set.index(coords)
    return False
