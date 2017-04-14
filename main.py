import math, os, sys, pygame
from pygame.locals import *
from chessboard import *
from valid_moves import valid_moves

pygame.init()
fps_clock = pygame.time.Clock()

display_width = 640
display_height = 640

title = 'Chess'
crashed = False

window_surface_obj = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('{0}'.format(title))


# adds png to sprite dictionary
def update_dict(sprite_name, dict):
    dict[sprite_name] = pygame.image.load('resources/{0}.png'.format(sprite_name))


# just blit rewritten for convenience
def render(x, y, sprite, dict):
    window_surface_obj.blit(dict[sprite], (x * 64 + 64, y * 64 + 64))


# returns normalized mouse coordinates
def normalize(position):
    return ([math.floor(position[0] / 64) - 1, math.floor(position[1] / 64) - 1])


# autofill dictionary with sprites from resources
image_dict = {}
for filename in os.listdir('resources'):
    if filename[-4:] == '.png':
        update_dict(filename[:-4], image_dict)

chessboard = [[-1, -1, 'board']] + checker('w_square', 'b_square')

pieces = fill_pieces('w_', 'b_')

current_piece = False
current_player = 0
players = {0: 'w', 1: 'b'}

while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = normalize(pygame.mouse.get_pos())
            if not current_piece:
                current_piece = search_piece(pos, players[current_player], pieces)
                if valid_moves(pieces[current_piece], pieces) == []:
                    current_piece = False
            elif current_piece == search_piece(pos, players[current_player], pieces):
                current_piece = False
            elif pos in valid_moves(pieces[current_piece], pieces):
                pieces[current_piece][0:2] = pos
                current_player = (current_player + 1) % 2
                current_piece = False
    for square in chessboard:
        render(square[0], square[1], square[2], image_dict)
    if current_piece:
        for square in valid_moves(pieces[current_piece], pieces):
            render(square[0], square[1], 'g_square', image_dict)
    for piece in pieces:
        render(piece[0], piece[1], piece[2], image_dict)
        for piece2 in pieces:
            if piece[0:2] == piece2[0:2] and piece[2] != piece2[2]:
                if current_player == 0:
                    if piece[2][0] == 'w':
                        pieces.remove(piece)
                    elif piece2[2][0] == 'w':
                        pieces.remove(piece2)
                if current_player == 1:
                    if piece[2][0] == 'b':
                        pieces.remove(piece)
                    elif piece2[2][0] == 'b':
                        pieces.remove(piece2)
    pygame.display.update()
    fps_clock.tick(30)
