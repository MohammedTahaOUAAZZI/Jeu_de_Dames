import pygame
from checkers.board import Board
from .constants import RED, WHITE

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}


    def reset(self):
        self._init()

    def select(self, row, col):
        pass

    def move(self, row, col):
        pass

