from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate, position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):



    else:


def get_all_moves(position, color, game):
