import os, sys, pygame
from pygame.locals import *
from chessboard import checker, fill_pieces
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


# autofill dictionary with sprites from resources
image_dict = {}
for filename in os.listdir('resources'):
    if filename[-4:] == '.png':
        update_dict(filename[:-4], image_dict)

chessboard = [[-1, -1, 'board']] + checker('w_square', 'b_square')

pieces = fill_pieces('w_', 'b_')

while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for square in chessboard:
        render(square[0], square[1], square[2], image_dict)
    for piece in pieces:
        render(piece[0], piece[1], piece[2], image_dict)
    pygame.display.update()
    fps_clock.tick(30)
