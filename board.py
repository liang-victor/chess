class ChessBoard:
    """A representation of game state

    self.pieces is a dictionary that keys positions to pieces

    todo: interface that is closer to chess notation

    """
    def __init__(self):
        self.pieces = {}
        self.out_of_play = set()
        self.min_x = 1
        self.max_x = 8
        self.min_y = 1
        self.max_y = 8
        self.turns = 0 # increase by 1 each turn

    def __getitem__(self, position):
        return self.pieces[position]

    def is_current_turn(self, piece):
        """Black allowed to move on even turns, white on odd turns"""
        if piece.is_black:
            return self.turns%2==0
        return self.turns%2==1

    def add_piece(self, piece):
        if piece.position not in self.pieces:
            self.pieces[piece.position] = piece
        else:
            raise "Position already occupied"

    def add_pieces(self, pieces):
        for piece in pieces:
            self.add_piece(piece)

    def within_bounds(self, position):
        return self.min_x <= position.real <= self.max_x and self.min_y <= position.imag <= self.max_y

    def make_move(self, start_position, move):
        piece = self.pieces[start_position]
        if move in piece.moves(self) and self.is_current_turn(piece):
            if move in self.pieces and piece.opposite_color(self.pieces[move]):
                removed = self.pieces.pop(move)
                self.out_of_play.add(removed)

            self.pieces.pop(piece.position)
            self.pieces[move] = piece
            piece.position = move

            self.turns += 1
        else:
            raise "Illegal Move"


def new_game_board():
    """Returns a game board populated with the standard starting position"""
    pass
