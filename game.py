"""Chess

components of the game
    - chess board
        - this is a grid (8x8)
        - we can represent positions as coordinates
            - complex numbers might be a nice way to handle 2D coordinates
    - pieces
        - 6 types of pieces
            - pawn: 1-2 forwards (move two if it's in the first move)
            - rook: any horizontal
            - knight: L shapes (can skip)
            - bishop: any diagonal
            - queen: any horizontal + any diagonal
            - king: 1 any direction

        - for a given piece, we should be able to calculate the possible moves

    - special rules (maybe skip these)
        - castling
        - en passant
        - promotion
"""