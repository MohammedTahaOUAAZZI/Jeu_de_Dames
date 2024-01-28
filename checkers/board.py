import pygame
from .constants import BLACK, ROWS, WHITE, SQUARE_SIZE, COLS, RED
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1 

    def get_piece(self, row, col):
        return self.board[row][col]
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col,  RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win) 
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        
        if piece.color == RED or piece.king:
            moves.update(self._traverse_left(row - 1,max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1,max(row - 3, -1), -1, piece.color, right))

        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1,min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1,min(row + 3, ROWS), 1, piece.color, right))
            return moves
    


        def _traverse_left(self, start, stop, step, color, left, skipped=[]):
            moves= {}
            last = []
            for r in range(start, stop, step):
                if left < 0:
                    break

                current = self.board.get_piece(r, left)
                if current == 0:
                    if skip_only and not last:
                        break
                    elif skip_only:
                        pass
                    else:
                        moves[(r, left)] = last      

                left -= 1

        def _traverse_right(self, start, stop, step, color, right, skipped=[]):
            pass

             
