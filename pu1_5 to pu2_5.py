from octics_squares import OcticSquares
from svg_export_utils import octic_squares2pdf

squares = OcticSquares(5)
# u^2 = x y (x+y) z (x+wy+z)
# STEP 0 - p25 point
squares.add_lines("P1", "23", [0, 0, 1, 1])
squares.add_lines("P1", "45", [0, 1, 1, 0])

squares.add_lines("P2", "13", [0, 0, 1, 1])
squares.add_lines("P2", "4", [0, 0.5, 1, 0.5])
squares.add_lines("P2", "5", [0, 1, 1, 0])

squares.add_lines("P3", "12", [0, 0, 1, 1])
squares.add_lines("P3", "4", [0, 0.5, 1, 0.5])
squares.add_lines("P3", "5", [0, 1, 1, 0])

squares.add_lines("P4", "1", [0, 0, 1, 1])
squares.add_lines("P4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("P4", "35", [0, 1, 1, 0])

squares.add_lines("P5", "1", [0, 0, 1, 1])
squares.add_lines("P5", "2", [0, 0.5, 1, 0.5])
squares.add_lines("P5", "45", [0, 1, 1, 0])

squares.remove_line("P1:23")
squares.add_lines("P1", "23", [0, 0.2, 1, 0.2])

octic_squares2pdf(squares, "new pu1_5 to pu2_5_0")
# STEP 1 - blow-up of the fivefold point

squares = OcticSquares(5, _IMG_SIZE=(800, 120))

squares.add_square("E1")

squares.add_lines("P1", "23", [0, 0.2, 1, 0.2])
squares.add_lines("P1", "45", [0, 0.8, 1, 0.8])

squares.add_lines("P2", "13", [0, 0.2, 1, 0.2])
squares.add_lines("P2", "4", [0, 0.5, 1, 0.5])
squares.add_lines("P2", "5", [0, 0.8, 1, 0.8])

squares.add_lines("P3", "12", [0, 0.2, 1, 0.2])
squares.add_lines("P3", "4", [0, 0.5, 1, 0.5])
squares.add_lines("P3", "5", [0, 0.8, 1, 0.8])

squares.add_lines("P4", "1", [0, 0.2, 1, 0.2])
squares.add_lines("P4", "2", [0, 0.5, 1, 0.5])
squares.add_lines("P4", "35", [0, 0.8, 1, 0.8])

squares.add_lines("P5", "1", [0, 0.2, 1, 0.2])
squares.add_lines("P5", "2", [0, 0.5, 1, 0.5])
squares.add_lines("P5", "45", [0, 0.8, 1, 0.8])


squares.add_lines("E1", "1", [0, 0.5, 1, 0.5])
squares.add_lines("E1", "2", [0.1, 0, 0.3, 1])
squares.add_lines("E1", "3", [0.3, 0, 0.1, 1])
squares.add_lines("E1", "4", [0, 1, 1, 0])
squares.add_lines("E1", "5", [0, 0, 1, 1])

octic_squares2pdf(squares, "new pu1_5 to pu2_5_1")

squares.add_square("E2")

squares

octic_squares2pdf(squares, "new pu1_5 to pu2_5_2")
