from pieces import Pawn, Rook, Knight, Bishop, Queen, King
from board import ChessBoard

def test_black_pawn_moves_empty_board():
    board = ChessBoard()
    piece = Pawn(4+4j, is_black=True)

    moves = piece.moves(board)
    assert len(moves) == 1
    assert 4+3j in moves

def test_black_pawn_moves_empty_board():
    board = ChessBoard()
    piece = Pawn(4+4j, is_black=False)

    moves = piece.moves(board)
    assert len(moves) == 1
    assert 4+5j in moves

def test_rook_on_empty_board():
    board = ChessBoard()
    piece = Rook(4 + 4j, is_black=True)

    moves = piece.moves(board)
    allowed_moves = {1+4j, 2+4j, 3+4j, 5+4j, 6+4j, 7+4j, 8+4j,
                     4+1j, 4+2j, 4+3j, 4+5j, 4+6j, 4+7j, 4+8j}

    assert set(moves) == allowed_moves