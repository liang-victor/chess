# todo: extract method to handle scanning moves vs fixed moves lists



class ChessPiece:
    def __init__(self, is_black):
        self.is_black = is_black

    def opposite_color(self, other_piece):
        return self.is_black != other_piece.is_black

class Pawn(ChessPiece):
    def __init__(self, position, **kwargs):
        super().__init__(**kwargs)
        self.position = position
        self.direction = self.get_direction()

    def get_direction(self):
        """Black moves down, white moves up"""
        if self.is_black:
            return 0-1j
        return 0+1j

    def moves(self, board):
        # todo: handle first move to allow two steps
        # todo: handle attack moves on diagonals
        all_moves = [self.position + self.direction]
        allowed_moves = []
        for potential_position in all_moves:
            if potential_position not in board.pieces:
                allowed_moves.append(potential_position)
        return allowed_moves


class Rook(ChessPiece):
    """Piece that moves horizontally"""
    def __init__(self, position, **kwargs):
        super().__init__(**kwargs)
        self.position = position

    def moves(self, board):
        valid_moves = []

        for direction in [1+0j, -1+0j, 0+1j, 0-1j]:
            current_position = self.position
            while True:
                current_position += direction
                if board.within_bounds(current_position):
                    piece_at_destination = board.pieces.get(current_position)

                    if not piece_at_destination:
                        valid_moves.append(current_position)
                    elif self.opposite_color(piece_at_destination):
                        valid_moves.append(current_position)
                        break
                    else:
                        break
                else:
                    break

        return valid_moves


class Knight(ChessPiece):
    def __init__(self, position, **kwargs):
        super().__init__(**kwargs)
        self.position = position

    def moves(self, board):
        valid_moves = []
        for direction in [1+3j, 1-3j, 3+1j, 3-1j, -1+3j, -1-3j, -3+1j, -3-1j]:
            potential_position = self.position + direction

            if board.within_bounds(potential_position):
                piece_at_destination = board.pieces.get(potential_position)
                if not piece_at_destination:
                    valid_moves.append(potential_position)
                elif self.opposite_color(piece_at_destination):
                    valid_moves.append(potential_position)

        return valid_moves


class Bishop(ChessPiece):
    def __init__(self, position, **kwargs):
        super().__init__(**kwargs)
        self.position = position


    def moves(self, board):
        valid_moves = []

        for direction in [1+1j, -1+1j, 1-1j, -1-1j]:
            current_position = self.position
            while True:
                current_position += direction
                if board.within_bounds(current_position):
                    piece_at_destination = board.pieces.get(current_position)

                    if not piece_at_destination:
                        valid_moves.append(current_position)
                    elif self.opposite_color(piece_at_destination):
                        valid_moves.append(current_position)
                        break
                    else:
                        break
                else:
                    break

        return valid_moves

class Queen(ChessPiece):
    def __init__(self, position, **kwargs):
        super().__init__(**kwargs)
        self.position = position

    def moves(self, board):
        valid_moves = []

        for direction in [1+0j, -1+0j, 0+1j, 0-1j, 1+1j, -1+1j, 1-1j, -1-1j]:
            current_position = self.position
            while True:
                current_position += direction
                if board.within_bounds(current_position):
                    piece_at_destination = board.pieces.get(current_position)

                    if not piece_at_destination:
                        valid_moves.append(current_position)
                    elif self.opposite_color(piece_at_destination):
                        valid_moves.append(current_position)
                        break
                    else:
                        break
                else:
                    break

        return valid_moves

class King(ChessPiece):
    def __init__(self, position, **kwargs):
        super().__init__(**kwargs)
        self.position = position

    def moves(self, board):
        valid_moves = []
        for direction in [1+0j, -1+0j, 0+1j, 0-1j, 1+1j, -1+1j, 1-1j, -1-1j]:
            potential_position = self.position + direction

            if board.within_bounds(potential_position):
                piece_at_destination = board.pieces.get(potential_position)
                if not piece_at_destination:
                    valid_moves.append(potential_position)
                elif self.opposite_color(piece_at_destination):
                    valid_moves.append(potential_position)

        return valid_moves