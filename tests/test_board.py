from board import ChessBoard
from pieces import Rook, Queen
import pytest

def test_attacking_move():
    board = ChessBoard()
    rook = Rook(4+4j, is_black=True)
    queen = Queen(5+4j, is_black=False)
    board.add_piece(rook)
    board.add_piece(queen)

    board.make_move(4+4j, 5+4j)

    assert queen in board.out_of_play
    assert board[5+4j] == rook
    assert rook.position == 5+4j

def test_move_out_of_bounds():
    board = ChessBoard()
    board.add_piece(Rook(4+4j, is_black=True))

    with pytest.raises(Exception):
        board.make_move(4+4j, 4+25j)

def test_move_onto_same_color():
    board = ChessBoard()
    board.add_piece(Rook(4 + 4j, is_black=True))
    board.add_piece(Queen(5 + 4j, is_black=False))

    with pytest.raises(Exception):
        board.make_move(4+4j, 5+4j)
