import math, os, sys, pygame, logging
from pygame.locals import *
from chessboard import *
from valid_moves import *
from copy import deepcopy

pygame.init()
fps_clock = pygame.time.Clock()

display_width = 960
display_height = 640

title = 'Chess'
crashed = False

white = pygame.Color(255, 255, 255)

window_surface_obj = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('{0}'.format(title))

font_obj = pygame.font.Font("resources/opensans-lightitalic.ttf", 15)


# adds png to sprite dictionary
def update_dict(sprite_name, dict):
    dict[sprite_name] = pygame.image.load('resources/{0}.png'.format(sprite_name))


# just blit rewritten for convenience
def render(x, y, sprite, dict):
    window_surface_obj.blit(dict[sprite], (x * 64 + 64, y * 64 + 64))


# returns normalized mouse coordinates
def normalize(position):
    return ([math.floor(position[0] / 64) - 1, math.floor(position[1] / 64) - 1])


# render a variable as text onscreen
def display_data(x, y, data, font, color):
    data_text = font.render("{0}".format(data), True, color)
    window_surface_obj.blit(data_text, (x, y))


# autofill dictionary with sprites from resources
image_dict = {}
for filename in os.listdir('resources'):
    if filename[-4:] == '.png':
        update_dict(filename[:-4], image_dict)

chessboard = [[-1, -1, 'board']] + checker('w_square', 'b_square')

pieces = fill_pieces('w_', 'b_')
pieces_last = deepcopy(pieces)

current_piece = False
current_player = 0
players = {0: 'w', 1: 'b'}

check = [0, 0]
checking_pieces = []
checked = False
checkmated = False
captured = False

moves = []
moves_formatted = []
moves_processed = []

logging.basicConfig(filename='GAMES.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info(': new game started.')

while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            logging.info(': game exited.')
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if not checkmated:
                pos = normalize(pygame.mouse.get_pos())
                if not current_piece:
                    current_piece = search_piece(pos, players[current_player], pieces)
                    if valid_moves(pieces[current_piece], pieces) == []:
                        current_piece = False
                elif current_piece == search_piece(pos, players[current_player], pieces):
                    current_piece = False
                elif pos in valid_moves(pieces[current_piece], pieces):
                    pieces[current_piece][0:2] = pos
                    if check_collision(pieces, (current_player + 1) % 2):
                        captured = True
                    else:
                        captured = False
                    check, checking_pieces = in_check(pieces)
                    if check[current_player]:
                        pieces = deepcopy(pieces_last)
                    else:
                        if check[(current_player + 1) % 2]:
                            checked = True
                            checkmated = in_checkmate(pieces, check)
                        else:
                            checked = False
                        moves.append([pieces[current_piece][2], pos, current_piece])
                        moves_formatted.append(format_move(moves[-1], captured, checked, checkmated))
                        moves_processed.append(log_moves(moves_formatted))
                        if log_moves(moves_formatted):
                            logging.info(log_moves(moves_formatted))
                        current_player = (current_player + 1) % 2
                        current_piece = False
                        pieces_last = deepcopy(pieces)
    for square in chessboard:
        render(square[0], square[1], square[2], image_dict)
    if current_piece:
        for square in valid_moves(pieces[current_piece], pieces):
            render(square[0], square[1], 'g_square', image_dict)
        render(pieces[current_piece][0], pieces[current_piece][1], 'g_square', image_dict)
    for piece in pieces:
        render(piece[0], piece[1], piece[2], image_dict)
    render(-1, -1, players[current_player] + '_king', image_dict)
    for move in moves_processed:
        display_data(645 + math.floor(moves_processed.index(move) / 60) * 40, moves_processed.index(move) * 10, move,
                     font_obj, white)
    pygame.display.update()
    fps_clock.tick(30)
